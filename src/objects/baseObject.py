from .interface import Mechanics
from pygame.sprite import Sprite
from pygame.rect import Rect
from pygame.surface import Surface


class BaseObject(Sprite):

    # variable name specified by pygame sprite
    rect: Rect
    image: Surface

    def __init__(self, rect: Rect, background: Surface) -> None:
        Sprite.__init__(self)
        self.rect = rect
        self.image = background


    def update(self) -> None:
        # drawing handled by sprite parent group class
        pass