import pygame
from typing import Callable
from ..utils import vec2d
from .items import BaseItem, TextHelper, Button


class BaseScene:

    group: pygame.sprite.Group
    items: list[BaseItem]
    registeredEvent: dict[int, list[Callable]]
    start: bool

    def __init__(self, description: str) -> None:

        self.group = pygame.sprite.Group()
        self.items = []
        self.registeredEvent = {}
        self.start = False

        pos = vec2d(1300, 20)
        settingText = TextHelper("Settings", tuple(pos))
        self.items.append(settingText)

        button = Button('start', (1300, 680))
        self.items.append(button)

        descriptionText = TextHelper(description, tuple(pos + vec2d(0, 40)), color=pygame.color.Color(128, 128, 128))
        self.items.append(descriptionText)


    def addGroup(self, *args: pygame.sprite.Sprite):
        for sprite in args:
            sprite.add(self.group)

    def drawAfterStart(self, surface: pygame.surface.Surface):
        pass

    def draw(self, surface: pygame.surface.Surface):

        if self.start:
            self.drawAfterStart(surface)
            self.group.update()
            self.group.draw(surface)

        self.handleEvent()
        self.drawSettings(surface)
        self.drawItems(surface)
        self.handleSetting()

    def handleSetting(self) -> None:
        assert isinstance(self.items[1], Button)
        self.start = self.items[1].activated

    def drawItems(self, surface: pygame.surface.Surface) -> None:
        for item in self.items:
            item.draw(surface, self.registeredEvent)

    def drawSettings(self, surface: pygame.surface.Surface):
        pygame.draw.rect(surface, (237, 201, 102), pygame.rect.Rect(1280, 0, 200, 720))

    def handleEvent(self):
        from pygame import locals

        for event in pygame.event.get():
            if self.registeredEvent.get(event.type) is not None:
                for f in self.registeredEvent[event.type]:
                    f(event)
            if event.type == locals.QUIT:
                quit()

        