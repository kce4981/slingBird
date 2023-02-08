from . import BaseScene
from ..objects import SingleParticle
from ..utils import vec2d
from .items import TextBox
import pygame


class Projectile(BaseScene):

    def __init__(self) -> None:
        super().__init__("")

        self.particle = SingleParticle(vec2d(30, 700))
        self.addGroup(self.particle)
        self.initVelocity = vec2d()

        self.angleTextBox = TextBox((1290, 150), "angle: degree", defualtValue='45')
        self.magnitudeTextBox = TextBox((1290, 250), "Magnitude: float", defualtValue='30')
        self.items.append(self.angleTextBox)
        self.items.append(self.magnitudeTextBox)

        self.shot = False
        self.clamped = False

        self.screen = pygame.surface.Surface((1280, 720))
        floorRect = pygame.rect.Rect(0, 715, 1280, 5)
        wallRect = pygame.rect.Rect(1275, 0, 5, 720)
        self.screen.fill((3, 111, 252), floorRect)
        self.screen.fill((3, 111, 252), wallRect)
        self.area = pygame.rect.Rect(0, 0, 1280, 715)
        self.screenRect = self.screen.get_rect()

    def drawAfterStart(self, surface: pygame.surface.Surface):

        if not self.shot:
            self.particle.mainParticle.velocity += self.initVelocity
            self.shot = True
        
        if not self.area.contains(self.particle.rect):
            self.clamped = True
            clampedRect = self.area.clamp(self.particle.rect)
            self.particle.mainParticle.velocity = vec2d()
            self.particle.mainParticle.pos = clampedRect.center

    def draw(self, surface: pygame.surface.Surface):
        surface.blit(self.screen, (0, 0))
        if not self.shot:
            arrowPos = self.particle.rect.centerx + self.initVelocity[0], self.particle.rect.centery + self.initVelocity[1]
            pygame.draw.line(surface, (255, 255, 255), self.particle.rect.center, arrowPos)
        return super().draw(surface)

    def handleSetting(self) -> None:
        magnitude = self.magnitudeTextBox.getContent(float, 1)
        angle = 360 - self.angleTextBox.getContent(float, 0.0)
        self.initVelocity = vec2d(1, 0).rotate(angle) * magnitude
        super().handleSetting()
