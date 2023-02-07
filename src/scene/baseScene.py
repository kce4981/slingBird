import pygame
from typing import Any, Callable

class BaseScene:

    _settings: dict = {}
    group: pygame.sprite.Group
    registeredEvent: dict[int, list[Callable]] = {}

    def __init__(self) -> None:
        self.group = pygame.sprite.Group()

    def addGroup(self, *args: pygame.sprite.Sprite):
        for sprite in args:
            sprite.add(self.group)

    def draw(self, surface: pygame.surface.Surface):
        self.group.update()
        self.group.draw(surface)
        self.handleEvent()

    def handleEvent(self):
        from pygame import locals

        for event in pygame.event.get():
            if self.registeredEvent.get(event.type) is not None:
                for f in self.registeredEvent[event.type]:
                    f()
            
            if event == locals.QUIT:
                pygame.quit()

    @property
    def settings(self) -> dict:
        return self._settings

    @settings.setter
    def settings(self, value: dict) -> None:
        self._settings = value

        