import pygame
from .baseItem import BaseItem
from . import Text


class TextBox(BaseItem):

    def __init__(self, rect: pygame.rect.Rect) -> None:
        
        self.rect = rect
        self.text = ''
        self.textHelper = Text(self.text, (self.rect.x, self.rect.y))
        self.registered = False
        self.quitEventBus = False

    def draw(self, surface: pygame.surface.Surface, eventSubList: dict[int, list]):
        from pygame import locals
        pygame.draw.rect(surface, (0, 0, 0), self.rect, width=2)

        self.textHelper = Text(self.text, (self.rect.x, self.rect.y))
        self.textHelper.draw(surface)

        if eventSubList.get(locals.KEYDOWN) is None:
            eventSubList[locals.KEYDOWN] = []
    
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            if not self.registered:
                eventSubList[locals.KEYDOWN].append(self.keyEventHandler)
                self.registered = True

        if self.quitEventBus:
            self.registered = False
            self.quitEventBus = False
            eventSubList[locals.KEYDOWN].remove(self.keyEventHandler)

    def keyEventHandler(self, event: pygame.event.Event):
        
        if event.key == 8:
            self.text = self.text[:-1]
            return

        self.text += event.unicode