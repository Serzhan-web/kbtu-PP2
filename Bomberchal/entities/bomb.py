import globals
from utils.helpers import rand, get_tick_from_ms, in_valid_range
from utils.sound_api import play_explosion_sound
from entities.entity import Entity
from entities.fire import Fire
from entities.interfaces.Collidable import Collidable
from entities.interfaces.Controllable import Controllable
from entities.interfaces.Movable import Movable


BOMB_KEY = "bomb"


class Bomb(Movable, Controllable, Collidable, Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._layer = globals.BASE_ENTITY_LAYER + 2
        self.entity_key = BOMB_KEY

        self.timer = kwargs.get("timer", get_tick_from_ms(0))  # in ticks
        self.power = kwargs.get("power", 1)
        self.spawner_key = kwargs.get("spawner_key", None)  # which entity spawned
        self.is_spawner_inside = True  # to ignore the collision when the bomb is spawned
        self.exploded = kwargs.get("exploded", False)
        self.spread_type = kwargs.get("spread_type", "bfs")  # | "star" | "up" | "right" | "down" | "left"

        if self.mounted:
            self.set_image_path(globals.bomb_frames[0])

    def add_tick(self):
        self.try_snapshot()
        self.tick += 1

        if not self.mounted:
            return

        if self.tick > self.timer:
            self.explode()

        if self.tick < self.timer // 3:
            self.set_image_path(globals.bomb_frames[0])
        elif self.tick < (self.timer // 3) * 2:
            self.set_image_path(globals.bomb_frames[1])
        else:
            self.set_image_path(globals.bomb_frames[2])

    def spread_fire(self, exploder_key):
        if not in_valid_range(self.x, self.y, len(globals.field_fire_state), len(globals.field_fire_state[0])) or globals.field_fire_state[self.x][self.y] > self.power:
            return

        npx_w = int(self.px_w * .8)
        npx_h = int(self.px_h * .8)
        dw = (self.px_w - npx_w) // 2
        dh = (self.px_h - npx_h) // 2
        fire = Fire(  # region parameters
            spread_type=self.spread_type,
            is_initial=True,
            power=self.power,
            timer=get_tick_from_ms(500),
            spread_timer=get_tick_from_ms(25),
            spawner_key=exploder_key,

            x=self.x,
            y=self.y,
            px_x=self.px_x + dw,
            px_y=self.px_y + dh,
            px_w=npx_w,
            px_h=npx_h,

            color=(rand(128, 256), 0, 0),
        )  # endregion

        if fire.spread_timer == 0:
            fire.spread()

    def explode(self, exploder_key=None):
        if self.exploded:
            return
        if exploder_key is None:
            exploder_key = self.spawner_key

        self.exploded = True
        play_explosion_sound(volume=.2)

        if self.spawner_key:
            spawner = globals.map_key_sprite[self.spawner_key]
            spawner.bomb_allowed += 1

        self.spread_fire(exploder_key)

        self.kill()


def get_bombs(entities):
    res = set()
    for entity in entities:
        if isinstance(entity, Bomb):
            res.add(entity)
    return res