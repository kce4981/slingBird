from .interface import Mechanics
from pygame.sprite import Sprite
from pygame.rect import Rect
from pygame.surface import Surface
from typing import Self
from ..utils import vec2d


class BaseObject(Sprite):

    # variable name specified by pygame sprite
    rect: Rect
    image: Surface

    def __init__(self, rect: Rect, background: Surface) -> None:
        Sprite.__init__(self)
        self.rect = rect
        self.image = background

    @classmethod
    def fromObject(cls, obj: 'BaseObject', *args):
        return cls(obj.rect, obj.image, *args)

    def move(self, offset: vec2d):
        newPos = vec2d(*self.rect.topleft) + offset
        newPos = round(newPos.x), round(newPos.y)
        self.rect.topleft = newPos



    def update(self) -> None:
        # drawing handled by sprite parent group class
        pass