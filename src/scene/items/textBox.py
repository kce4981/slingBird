import pygame
from .baseItem import BaseItem


class TextBox(BaseItem):

    def __init__(self, rect: pygame.rect.Rect) -> None:
        
        self.box = rect

    def draw(self, surface: pygame.surface.Surface):
        pygame.draw.rect(surface, (0, 0, 0), self.box, width=2)
    