import pygame
from pygame.font import Font
from .baseItem import BaseItem

FONT_FACE = pygame.font.get_default_font()
DEFAULT_COLOR = pygame.color.Color(0, 0, 0)

class Text(BaseItem):

    def __init__(self, string: str, pos: tuple, size: int=24, color=DEFAULT_COLOR) -> None:
        
        self.string = string
        self.font = Font(FONT_FACE, size)
        self.pos = pos
        self.color = color

    def getSurface(self) -> pygame.surface.Surface:
        return self.font.render(self.string, True, self.color)


    def draw(self, surface: pygame.surface.Surface, *args):
        surface.blit(self.getSurface(), self.pos)
