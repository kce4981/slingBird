import pygame
from typing import Any, Callable
from ..utils import vec2d
from .items import BaseItem, TextBox

class BaseScene:

    _settings: dict = {}
    group: pygame.sprite.Group
    items: list[BaseItem]
    registeredEvent: dict[int, list[Callable]] = {}

    def __init__(self) -> None:
        self.group = pygame.sprite.Group()
        self.items = []

    def addGroup(self, *args: pygame.sprite.Sprite):
        for sprite in args:
            sprite.add(self.group)

    def draw(self, surface: pygame.surface.Surface):
        self.group.update()
        self.group.draw(surface)
        self.handleEvent()
        self.drawSettings(surface)
        self.drawItems(surface)

    def drawItems(self, surface: pygame.surface.Surface) -> None:
        for item in self.items:
            item.draw(surface)

    def drawSettings(self, surface: pygame.surface.Surface):
        from pygame.font import Font
        from .items import TextBox
        pos = vec2d(1300, 20)
        pygame.draw.rect(surface, (237, 201, 102), pygame.rect.Rect(1280, 0, 200, 720))

        font = Font(pygame.font.get_default_font(), 24)
        settingText = font.render("Settings", True, (0, 0, 0))
        textBoxRect = pygame.rect.Rect(pos[0], pos[1] + 50, 150, 20)
        textBox = TextBox(textBoxRect)
        self.items.append(textBox)
        surface.blit(settingText, pos)

    def handleEvent(self):
        from pygame import locals

        for event in pygame.event.get():
            if self.registeredEvent.get(event.type) is not None:
                for f in self.registeredEvent[event.type]:
                    f()
            print(event)
            if event == locals.QUIT:
                pygame.quit()

    @property
    def settings(self) -> dict:
        return self._settings

    @settings.setter
    def settings(self, value: dict) -> None:
        self._settings = value

        