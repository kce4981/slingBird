from abc import abstractmethod
import pygame

class BaseItem:

    @abstractmethod
    def draw(self, surface: pygame.surface.Surface):
        pass