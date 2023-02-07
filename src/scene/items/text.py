import pygame
from pygame.font import Font
from .baseItem import BaseItem

FONT_FACE = pygame.font.get_default_font()

class Text(BaseItem):

    def __init__(self, string: str, pos: tuple[int, int], size: int=48) -> None:
        
        self.string = string
        self.font = Font(FONT_FACE, size)
        self.pos = pos

    def getSurface(self) -> pygame.surface.Surface:
        return self.font.render(self.string, antialias=True, color=(0, 0, 0))


    def draw(self, surface: pygame.surface.Surface):
        surface.blit(self.getSurface(), self.pos)
