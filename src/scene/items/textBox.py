import pygame
from .baseItem import BaseItem
from . import TextHelper
from ...utils import vec2d


class TextBox(BaseItem):

    def __init__(self, pos: tuple[int | float, int | float], title: str, defualtValue='') -> None:
        
        self.rect = pygame.rect.Rect(*pos, 200, 20)
        self.content = defualtValue
        self.titleHelper = TextHelper(title, tuple(vec2d(*self.rect.topleft) - vec2d(0, 30)))
        self.textHelper = TextHelper(self.content, (self.rect.x, self.rect.y))
        self.registered = False
        self.quitEventBus = False

    def draw(self, surface: pygame.surface.Surface, eventSubList: dict[int, list]):
        from pygame import locals

        self.titleHelper.draw(surface)

        pygame.draw.rect(surface, (0, 0, 0), self.rect, width=2)

        self.textHelper = TextHelper(self.content, (self.rect.x, self.rect.y))
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
        
        # backspace
        if event.key == 8:
            self.content = self.content[:-1]
            return

        # esc key
        if event.key == 27:
            self.quitEventBus = True
            return

        self.content += event.unicode

    def getContent(self, type: type, defaultValue):
        try:
            get = type(self.content)
        except ValueError:
            return defaultValue
        else:
            return get