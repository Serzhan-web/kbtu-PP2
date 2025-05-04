import globals
import os
import pygame

from utils.helpers import get_tick_from_ms, rand


def format_surface_id_to_key(surface_id):
    return "sid_" + str(surface_id)


class SurfaceSprite(pygame.sprite.Sprite):
    SurfaceId = 0

    def __init__(self, **kwargs):
        super().__init__()
        self.kwargs = kwargs

        self.px_x = kwargs.get("px_x", 0)  # position x in pixels (from left) [пиксельные коорды]
        self.px_y = kwargs.get("px_y", 0)  # position y in pixels (from top) [пиксельные коорды]
        self.px_w = kwargs.get("px_w", 1)  # width in pixels
        self.px_h = kwargs.get("px_h", 1)  # height in pixels
        self.image_size = kwargs.get("image_size", (self.px_w, self.px_h))  # sizes of image, does not affect to physical interactions of an object

        self.color = kwargs.get("color", (rand(128, 256), 0, rand(128, 256)))
        self.layer = kwargs.get("layer", 0)  # Like z-index in CSS
        self._layer = self.layer

        self.surface_id = SurfaceSprite.SurfaceId
        self.ignore_collision = kwargs.get("ignore_collision", False)
        self.dynamic = kwargs.get("dynamic", False)  # is only for one frame
        self.key = kwargs.get("key", format_surface_id_to_key(self.surface_id))
        SurfaceSprite.SurfaceId += 1

        self.should_mount = kwargs.get("should_mount", True)
        self.mounted = False  # physically visible in screen
        self.hidden = kwargs.get("hidden", False)  # visually visible in screen

        self.image_path = kwargs.get("image_path", None)
        self.align = kwargs.get("align", "topleft")

        self.image = None
        self.rect = None
        self.should_refresh = False
        if kwargs.get("should_refresh", True):
            self.refresh()

        if not self.mounted and self.should_mount:
            self.mount()

    def refresh(self):  # NOTE: it is expensive operation if this sprite has an image
        # print("REQUESTED REFRESH")
        self.image = pygame.Surface([self.px_w, self.px_h], pygame.SRCALPHA)  # SRCALPHA will ensure that blit png image will be transparent

        if self.image_path is not None and os.path.exists(self.image_path):
            image_dw = (self.px_w - self.image_size[0]) // 2
            image_dh = (self.px_h - self.image_size[1]) // 2

            self.image.blit(
                pygame.transform.scale(
                    pygame.image.load(self.image_path),
                    self.image_size,
                ),
                (image_dw, image_dh)
            )
        else:
            self.image.set_colorkey((0, 0, 0))  # color to make transparent
            self.image.fill(self.color)  # Color of surface
            pygame.draw.rect(self.image, self.color, pygame.Rect((0, 0, self.px_w, self.px_h)))
        
        self.rect = self.image.get_rect()
        self.rect.x = self.px_x
        self.rect.y = self.px_y

        if self.align == "center":
            self.rect.x -= self.rect.width // 2
            self.rect.y -= self.rect.height // 2

        if self.mounted:
            self.mount()

    def set_image_path(self, image_path, size=None):
        if size is None:
            size = self.image_size
        if self.image_path == image_path and self.image_size == size:
            return
        self.image_path = image_path
        self.image_size = size
        self.should_refresh = True

    def unmount(self):
        unmount(self)

    def mount(self):
        return mount_sprite(self)

    def move_px(self, x=0, y=0):
        self.px_x += x
        self.px_y += y
        self.rect.x += x
        self.rect.y += y

    def set_px(self, x=0, y=0):
        self.px_x = x
        self.px_y = y
        self.rect.x = x
        self.rect.y = y

    def collides_with(self, sprite2):
        return self.mounted and sprite2.mounted and pygame.sprite.collide_rect(self, sprite2)


class TextSprite(SurfaceSprite):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, should_refresh=False)
        self.font_size = kwargs.get("key", None)
        self.color = kwargs.get("color", (0, 0, 0))
        self.font_size = kwargs.get("font_size", 14)
        self.font = kwargs.get("font_family", globals.TEXT_FONT)
        self.text = kwargs.get("text", "-")
        self.align = kwargs.get("align", "topleft")
        self.text_rect = None

        self.font_obj = pygame.font.Font(self.font, self.font_size)

        if kwargs.get("should_refresh", True):
            self.refresh()

    def refresh(self):
        self.image = self.font_obj.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.x = self.px_x
        self.rect.y = self.px_y

        if self.align == "center":
            self.rect.x -= self.rect.width // 2
            self.rect.y -= self.rect.height // 2

    def set_text(self, text):
        if self.text == text:
            return

        self.text = text
        self.should_refresh = True

    def set_color(self, color):
        if self.color == color:
            return

        self.color = color
        self.should_refresh = True


class GIFSprite(SurfaceSprite):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, should_refresh=False)
        self.delay = get_tick_from_ms(kwargs.get("delay", 300))  # задержка между кадрами в мс
        self.last_update = float("-inf")
        self.current_frame = 0
        self.frames = kwargs.get("frames", [])  # image paths
        if len(self.frames) == 0:
            raise "No frames provided for GifSprite"
        self.process_gif()

    def process_gif(self):
        now = globals.tick
        if now - self.last_update > self.delay:
            self.last_update = now

            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.set_image_path(self.frames[self.current_frame])


def _get_sprite(constructor, **kwargs):
    # allowed constructors: SurfaceSprite, TextSprite, GIFSprite
    # if surface_id is not specified, generate a new surface with its unique id
    # otherwise, try to get surface from globals.map_key_sprite with this surface_id
    key = kwargs.get("key", None)

    if key not in globals.to_render_keys:
        sprite = constructor(**kwargs)
        # print("Rendered", sprite.key)
    else:
        sprite = globals.map_key_sprite[key]

    return sprite


def mount_rect(**kwargs):
    # key should be specified in order to decrease the number of renders
    # otherwise a new surface will be created and rendered each frame
    sprite = _get_sprite(SurfaceSprite, **kwargs)

    return sprite.mount()


def mount_text(**kwargs):
    # key should be specified in order to decrease the number of renders
    # otherwise a new surface will be created and rendered each frame
    sprite = _get_sprite(TextSprite, **kwargs)

    return sprite.mount()


def mount_gif(**kwargs):
    # key should be specified in order to decrease the number of renders
    # otherwise a new surface will be created and rendered each frame
    sprite = _get_sprite(GIFSprite, **kwargs)

    return sprite.mount()


def mount_button(**kwargs):
    key = kwargs.get("key")
    popup_layer = kwargs.get("popup_layer", 0)

    button = mount_rect(  # region parameters
        px_x=kwargs.get("px_x"),
        px_y=kwargs.get("px_y"),
        px_w=kwargs.get("px_w"),
        px_h=kwargs.get("px_h"),
        layer=globals.LAYER_SHIFT * popup_layer + globals.BUTTON_LAYER,
        align="center",
        image_path="Bomberchal/assets/images/buttons/bar_button.png",

        dynamic=kwargs.get("dynamic"),
        key=f"button_{key}",
    )  # endregion
    pos = button.px_x, button.px_y
    button_text = mount_text(  # region parameters
        px_x=pos[0],
        px_y=pos[1],
        layer=globals.LAYER_SHIFT * popup_layer + globals.TEXT_LAYER,
        align="center",
        text=kwargs.get("text"),
        font_size=kwargs.get("font_size"),
        color=kwargs.get("color", (255, 255, 255)),

        dynamic=kwargs.get("dynamic"),
        key=f"button_text_{key}",
    )  # endregion
    button_text_shadow = mount_text(  # region parameters
        px_x=pos[0] + globals.SHADOW_OFFSET,
        px_y=pos[1] + globals.SHADOW_OFFSET,
        layer=globals.LAYER_SHIFT * popup_layer + globals.SHADOW_LAYER,
        align="center",
        text=button_text.text,
        font_size=button_text.font_size,
        color=globals.SHADOW_COLOR,

        dynamic=kwargs.get("dynamic"),
        key=f"button_shadow_{key}",
    )  # endregion

    return [button, button_text, button_text_shadow]


def mount_sprite(sprite):
    if sprite.key in globals.to_render_keys:
        # already in to render queue
        return sprite

    # print("Rendered", sprite.key)

    globals.all_sprites.add(sprite)
    globals.map_key_sprite[sprite.key] = sprite
    globals.to_render_keys.add(sprite.key)
    sprite.mounted = True

    return sprite


def unmount(obj):
    if isinstance(obj, str):
        key = obj
        sprite = globals.map_key_sprite[key]
    elif isinstance(obj, SurfaceSprite):
        sprite = obj
        key = sprite.key
    else:
        raise "Trying to unmount unknown type"

    globals.all_sprites.remove(sprite)
    globals.to_render_keys.discard(key)
    sprite.mounted = False

    return sprite


def refill_screen():
    if globals.current_page in ("Bomberchal/pages/menu/settings", "Bomberchal/pages/menu/scoreboard", "Bomberchal/pages/menu/customization", "Bomberchal/pages/menu/play") and \
       globals.brown_background_img:
        globals.DISPLAYSURF.blit(globals.brown_background_img, (0, 0))
    elif globals.current_page == "menu" and globals.menu_background_img:
        globals.DISPLAYSURF.blit(globals.menu_background_img, (0, 0))
    else:
        globals.DISPLAYSURF.fill((0, 0, 20))


def reset_frame():
    from entities.entity import Entity

    globals.to_render_keys.clear()
    globals.map_key_sprite.clear()
    globals.state_snapshots.clear()
    for sprite in globals.all_sprites.sprites():
        if isinstance(sprite, Entity):
            sprite.kill(True)
        else:
            sprite.kill()
    globals.all_sprites.empty()


def draw_sprites():
    for sprite in globals.all_sprites.sprites():
        if sprite.key not in globals.to_render_keys:
            globals.all_sprites.remove(sprite)
            globals.to_render_keys.discard(sprite.key)
        else:
            if sprite.should_refresh:
                sprite.refresh()
                sprite.should_refresh = False

                sprite.should_refresh = False

        # all_sprites.update()

    will_return = []
    will_remove = []
    for sprite in list(globals.all_sprites.sprites()):
        if sprite.dynamic:
            will_remove.append(sprite)
        elif sprite.hidden:
            will_return.append(sprite)
            globals.all_sprites.remove(sprite)

    refill_screen()
    globals.all_sprites.draw(globals.DISPLAYSURF)
    globals.Frame.tick(globals.FPS)

    if globals.time_reversing_count_down:
        grey_overlay = pygame.Surface((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT), pygame.SRCALPHA)
        grey_overlay.fill((128, 128, 128, 128))
        globals.DISPLAYSURF.blit(grey_overlay, (0, 0))
    if globals.time_slowdown_count_down:
        brown_overlay = pygame.Surface((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT), pygame.SRCALPHA)
        brown_overlay.fill((255, 64, 0, 64))
        globals.DISPLAYSURF.blit(brown_overlay, (0, 0))
    pygame.display.flip()

    for sprite in will_remove:
        globals.all_sprites.remove(sprite)
        globals.to_render_keys.discard(sprite.key)

    for sprite in will_return:
        globals.all_sprites.add(sprite)
        globals.all_sprites.change_layer(sprite, sprite._layer)