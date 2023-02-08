from . import BaseItem, TextHelper
import pygame

COLOR_ACTIVATE = pygame.color.Color(82, 217, 67)
COLOR_DEACTIVATE = pygame.color.Color(217, 67, 67)

class Button(BaseItem):

    def __init__(self, header: str, pos: tuple) -> None:

        self.pos = pos
        self.activated = False
        self.last = False
        self.textHelper = TextHelper(header, self.pos)
    
    def draw(self, surface: pygame.surface.Surface, eventSubList: dict[int, list]):
        
        self.textHelper.draw(surface)
        color = COLOR_ACTIVATE if self.activated else COLOR_DEACTIVATE
        buttonPos = self.pos[0] + 150, self.pos[1] + 15
        rect = pygame.draw.circle(surface, color, buttonPos, 15)

        status = pygame.mouse.get_pressed()[0]
        if not self.last and status and rect.collidepoint(pygame.mouse.get_pos()):
            self.activated = not self.activated

        self.last = status