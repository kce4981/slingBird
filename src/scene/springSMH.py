from . import BaseScene
from ..objects import Spring, SingleParticle
from ..utils import vec2d
import pygame

class SpringSMH(BaseScene):

    def __init__(self) -> None:
        super().__init__("Draggable")

        pos = vec2d(640, 300)

        self.singleParticle = SingleParticle(pos, color=pygame.color.Color(0, 140, 255))
        self.spring = Spring(pos - vec2d(0, 100), self.singleParticle.mainParticle, 1.0, length=50)

        self.addGroup(self.singleParticle, self.spring)

        self.graphBackground = pygame.surface.Surface((1280, 720))
        self.graphBackground.fill((255, 255, 255))

        # breaks when offset > screen.width which is 256000
        # let's hope no one runs out of screen 
        self.graph = pygame.surface.Surface((256000, 720))
        self.graph.set_colorkey((0, 0, 0))
        self.offset = vec2d(640, 0)
        
    def drawAfterStart(self, surface: pygame.surface.Surface):
        surface.blit(self.graphBackground, (0, 0))
        pygame.draw.circle(self.graph, (17, 0, 255), (self.singleParticle.rect.centerx + self.offset[0], self.singleParticle.rect.centery), 5)

        self.offset += vec2d(1, 0)
        surface.blit(self.graph, (-self.offset[0], 0))

    def draw(self, surface: pygame.surface.Surface):
        return super().draw(surface)
        