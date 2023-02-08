from . import BaseScene
from ..objects import SingleParticle
from ..utils import vec2d
from .items import TextBox, TextHelper
import pygame
import math


class Projectile(BaseScene):

    def __init__(self) -> None:
        super().__init__("")

        self.particle = SingleParticle(vec2d(30, 700))
        self.addGroup(self.particle)
        self.initVelocity = vec2d()

        self.angleTextBox = TextBox((1290, 150), "angle: degree", defualtValue='45')
        self.magnitudeTextBox = TextBox((1290, 250), "Magnitude: float", defualtValue='100')
        self.items.append(self.angleTextBox)
        self.items.append(self.magnitudeTextBox)

        self.shot = False
        self.clamped = False

        self.initHeight = self.particle.rect.centery
        self.maxHeight = TextHelper("-1", (1290, 300), prompt='Height:')
        self.items.append(self.maxHeight)

        self.initWidth = self.particle.rect.centerx
        self.maxWidth = TextHelper("0", (1290, 350), prompt='width:')
        self.items.append(self.maxWidth)

        self.screen = pygame.surface.Surface((1280, 720))
        floorRect = pygame.rect.Rect(0, 715, 1280, 5)
        wallRect = pygame.rect.Rect(1275, 0, 5, 720)
        self.screen.fill((3, 111, 252), floorRect)
        self.screen.fill((3, 111, 252), wallRect)
        self.area = pygame.rect.Rect(0, 0, 1280, 715)
        self.screenRect = self.screen.get_rect()

        self.time = TextHelper('-1', (1290, 400), prompt='Time (sec): ')
        self.items.append(self.time)
        self.clock = pygame.time.Clock()
        self.clockActivated = False

    def drawAfterStart(self, surface: pygame.surface.Surface):

        # in pygame, y goes down when upwards
        maxHeight = max(int(self.maxHeight.text), self.initHeight - self.particle.rect.centery)
        self.maxHeight.text = str(maxHeight)

        maxWidth = max(int(self.maxWidth.text), self.particle.rect.centerx - self.initWidth)
        self.maxWidth.text = str(maxWidth)

        if not self.shot:
            self.particle.mainParticle.velocity += self.initVelocity
            self.shot = True
        
        if not self.area.contains(self.particle.rect):
            self.clamped = True
            clampedRect = self.area.clamp(self.particle.rect)
            self.particle.mainParticle.velocity = vec2d()
            self.particle.mainParticle.pos = clampedRect.center

        x = self.particle.rect.centerx
        # print(1280 - self.getIdealGraph(x), self.particle.rect.center[1])
        idealGraphPos = (x, self.initHeight - self.getIdealGraph(x))
        myEvalGraphPos = self.particle.rect.center
        # print(idealGraphPos, myEvalGraphPos)
        pygame.draw.circle(self.screen, (235, 52, 91), idealGraphPos, 1)
        pygame.draw.circle(self.screen, (49, 111, 235), myEvalGraphPos, 1)

        if not self.clockActivated and self.clockActivated is not None:
            self.clock.tick()
            self.clockActivated = True

        if self.initHeight == self.particle.rect.centery and self.clockActivated or self.clamped:
            t = max(float(self.time.text), self.clock.tick() / 1000)
            self.time.text = str(t)
            self.clockActivated = None

    def getIdealGraph(self, x: int) -> float:
        from ..utils import ConfigLoader

        g = ConfigLoader.gravityConstant
        rad = math.radians(self.angleTextBox.getContent(int, 0))
        v0 = self.initVelocity.magnitude_squared()
        y = math.tan(rad) * x - (g / (2 * v0 * math.cos(rad)**2)) * x**2
        return y

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
