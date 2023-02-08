import pygame
from pygame.font import Font
from .baseItem import BaseItem

FONT_FACE = pygame.font.get_default_font()
DEFAULT_COLOR = pygame.color.Color(0, 0, 0)

class TextHelper(BaseItem):

    _text: str

    def __init__(self, text: str, pos: tuple, size: int=24, color=DEFAULT_COLOR, prompt: str='') -> None:
        
        self.text = text
        self.font = Font(FONT_FACE, size)
        self.pos = pos
        self.color = color
        self.prompt = prompt

    def getSurface(self) -> pygame.surface.Surface:
        return self.font.render(self.prompt + self.text, True, self.color)


    def draw(self, surface: pygame.surface.Surface, *args):
        surface.blit(self.getSurface(), self.pos)


    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        self._text = value