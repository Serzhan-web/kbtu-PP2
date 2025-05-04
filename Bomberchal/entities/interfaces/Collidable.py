import globals
from entities.interfaces.BonusCollectable import BonusCollectable
from utils.helpers import rand
from entities.entity import Entity


class Collidable(Entity):
    def get_collisions(self):
        res = []

        for entity in globals.entities:
            if entity == self:
                continue
            if entity.collides_with(self):
                res.append(entity)

        return res

    def handle_collision(self):
        from entities.interfaces.BombSpawnable import BombSpawnable
        from entities.bomb import Bomb
        from entities.bots.original_bot import Bot
        from entities.fire import Fire
        from entities.bonus import Bonus
        from entities.player import Player
        from entities.obstacle import Obstacle
        from entities.interfaces.Movable import Movable

        if self.ignore_collision:
            return

        for entity in list(globals.entities):
            if entity.ignore_collision:
                continue

            if entity == self or not entity.collides_with(self):
                if isinstance(self, Bomb) and isinstance(entity, BombSpawnable) and self.spawner_key == entity.key:
                    self.is_spawner_inside = False
                continue
            # now entity collides and it is not ourselves

            if isinstance(self, Bot):
                if isinstance(entity, Player):
                    entity.make_damage(1, self.key)
                elif isinstance(entity, Bomb) and entity.spawner_key == self.key:
                    continue

            if isinstance(self, Movable):
                if isinstance(entity, Obstacle):
                    self_c_x = self.px_x + self.px_w // 2
                    self_c_y = self.px_y + self.px_h // 2
                    ent_c_x = entity.px_x + entity.px_w // 2
                    ent_c_y = entity.px_y + entity.px_h // 2

                    c_dx = self_c_x - ent_c_x
                    c_dy = self_c_y - ent_c_y

                    if abs(c_dx) == abs(c_dy):
                        if rand(0, 2) == 0:
                            self.adjust_from_x(entity)
                        else:
                            self.adjust_from_y(entity)

                    elif abs(c_dx) < abs(c_dy):
                        self.adjust_from_y(entity)
                    else:
                        self.adjust_from_x(entity)
                elif isinstance(entity, Bomb):
                    if entity.spawner_key == self.key and entity.is_spawner_inside:
                        continue  # ignore collision because the bomb was spawned immediately in spawner's position

                    self_c_x = self.px_x + self.px_w // 2
                    self_c_y = self.px_y + self.px_h // 2
                    ent_c_x = entity.px_x + entity.px_w // 2
                    ent_c_y = entity.px_y + entity.px_h // 2

                    c_dx = self_c_x - ent_c_x
                    c_dy = self_c_y - ent_c_y

                    if abs(c_dx) == abs(c_dy):
                        if rand(0, 2) == 0:
                            self.adjust_from_x(entity)
                        else:
                            self.adjust_from_y(entity)

                    elif abs(c_dx) < abs(c_dy):
                        self.adjust_from_y(entity)
                    else:
                        self.adjust_from_x(entity)

            if isinstance(self, BonusCollectable):
                if isinstance(entity, Bonus) and self.map_allowed_bonus_types[entity.type]:
                    self.collect(entity)

            if isinstance(self, Fire):
                if isinstance(entity, Obstacle):
                    self.kill()
                    entity.make_damage(1, self.spawner_key)
                elif isinstance(entity, Bomb):
                    self.kill()
                    entity.explode(self.spawner_key)
                elif isinstance(entity, Player) or isinstance(entity, Bot):
                    entity.make_damage(1, self.spawner_key)

    def adjust_from(self, entity):
        self.adjust_from_x(entity)
        self.adjust_from_y(entity)

    def adjust_from_x(self, entity):
        ent_px_w = entity.px_w
        ent_px_start_x = entity.px_x
        ent_px_end_x = entity.px_x + ent_px_w
        if self.px_x + (self.px_w // 2) < ent_px_start_x + (ent_px_w // 2):
            # print("ADJUSTED TO LEFT")
            # All copyrights were reserved by Kanich, Adilet, Lev
            self.set_px(ent_px_start_x - self.px_w, self.px_y)  # set lefter entity
        else:
            # print("ADJUSTED TO RIGHT")
            self.set_px(ent_px_end_x, self.px_y)  # set righter entity

    def adjust_from_y(self, entity):
        ent_px_h = entity.px_h
        ent_px_start_y = entity.px_y
        ent_px_end_y = entity.px_y + ent_px_h
        if self.px_y + (self.px_h // 2) < ent_px_start_y + (ent_px_h // 2):
            # print("ADJUSTED TO ABOVE")
            self.set_px(self.px_x, ent_px_start_y - self.px_h)  # set above entity
        else:
            # print("ADJUSTED TO BELOW")
            self.set_px(self.px_x, ent_px_end_y)  # set below entity