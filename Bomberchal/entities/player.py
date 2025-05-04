import globals
from utils.helpers import get_tick_from_ms
from entities.interfaces.BonusCollectable import BonusCollectable
from entities.entity import Entity
from entities.interfaces.BombSpawnable import BombSpawnable
from entities.interfaces.Collidable import Collidable
from entities.interfaces.Controllable import Controllable
from entities.interfaces.Movable import Movable


PLAYER_KEY = "player"


class Player(BonusCollectable, Collidable, Controllable, BombSpawnable, Movable, Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._layer = globals.BASE_ENTITY_LAYER + 5
        self.entity_key = PLAYER_KEY

        self.damage_countdown = kwargs.get("damage_countdown", get_tick_from_ms(3000))
        self.character_skin_key = kwargs.get("character_skin_key", "ch1")
        self.player_id = kwargs.get("player_id")
        if self.player_id is None:
            raise "player_id must be specified!"

        self.image_size = self.px_w + 16, self.px_h
        self.set_image_path(globals.character_frames[self.character_skin_key]["top_static"][0])

    def add_tick(self):
        self.try_snapshot()
        self.tick += 1

        if self.moved_this_frame:
            image_key = f"{self.last_direction}_moving"
            idx = (self.tick // 8) % len(globals.character_frames[self.character_skin_key][image_key])
            self.set_image_path(globals.character_frames[self.character_skin_key][image_key][idx])
        else:
            image_key = f"{self.last_direction}_static"
            idx = (self.tick // 8) % len(globals.character_frames[self.character_skin_key][image_key])
            self.set_image_path(globals.character_frames[self.character_skin_key][image_key][idx])

        if self.cur_damage_countdown > 0:
            self.hidden = self.cur_damage_countdown % 8 < 4
        else:
            self.hidden = False

        # FOR TESTING
        # if self.moved_this_frame:
        #     image_key = f"{self.last_direction}_moving"
        #     idx = (self.tick // 8) % len(globals.bot_frames["boss"][image_key])
        #     self.set_image_path(globals.bot_frames["boss"][image_key][idx])
        # else:
        #     image_key = f"{self.last_direction}_static"
        #     idx = (self.tick // 8) % len(globals.bot_frames["boss"][image_key])
        #     self.set_image_path(globals.bot_frames["boss"][image_key][idx])

    # def kill(self):  # noclip
    #     return

def get_players(entities):
    res = set()
    for entity in entities:
        if isinstance(entity, Player):
            res.add(entity)
    return res