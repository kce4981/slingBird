from . import BaseScene
from .items import TextBox, TextHelper, Button
from ..objects import Spring, SingleParticle
from ..utils import Kilogram, vec2d
import pygame
from math import pi, isclose

class SpringSMH(BaseScene):

    def __init__(self) -> None:
        super().__init__("Draggable")

        pos = vec2d(640, 300)

        SPRING_CONSTANT = 1.0
        MASS = Kilogram(5)

        self.singleParticle = SingleParticle(pos, color=pygame.color.Color(0, 140, 255), mass=MASS)
        self.spring = Spring(pos - vec2d(0, 100), self.singleParticle.mainParticle, SPRING_CONSTANT)
        self.addGroup(self.singleParticle, self.spring)

        self.massTextBox = TextBox((1290, 150), 'Mass (kg): float', '1')
        self.items.append(self.massTextBox)

        self.graphBackground = pygame.surface.Surface((1280, 720))
        self.graphBackground.fill((255, 255, 255))

        self.amplitudeText = TextHelper('0', (1290, 200), prompt='amp: ')
        self.items.append(self.amplitudeText)
        self.max = -9999999999
        self.min = 99999999999

        self.resetAmpBox = Button('Reset Amp', (1290, 250))
        self.items.append(self.resetAmpBox)

        self.period = TextHelper('0', (1290, 300), prompt='T (sec): ')
        self.items.append(self.period)
        self.clock = pygame.time.Clock()
        self.recordClock = False

        self.angularVelocity = TextHelper('0', (1290, 350), prompt='ω:')
        self.items.append(self.angularVelocity)

        self.velocityMax = TextHelper('0', (1290, 400), prompt='Vmax: ')
        self.items.append(self.velocityMax)
        self.vMax = -9999999

        # breaks when offset > screen.width which is 256000
        # let's hope no one runs out of screen 
        self.graph = pygame.surface.Surface((256000, 720))
        self.graph.set_colorkey((0, 0, 0))
        self.offset = vec2d(640, 0)
        
    def drawAfterStart(self, surface: pygame.surface.Surface):
        surface.blit(self.graphBackground, (0, 0))
        xPos = self.singleParticle.rect.centerx + self.offset[0]
        yPos = self.singleParticle.rect.centery
        pygame.draw.circle(self.graph, (17, 0, 255), (xPos, yPos), 5)

        self.max = max(self.max, yPos)
        self.min = min(self.min, yPos)
        self.amplitudeText.text = str((self.max - self.min) / 2)

        self.vMax = max(self.vMax, self.singleParticle.mainParticle.velocity.magnitude())
        self.velocityMax.text = str(self.vMax)

        if self.max == yPos:
            self.recordClock = True
            self.clock.tick()
        
        if self.min == yPos and self.recordClock:
            self.recordClock = False
            timeSpan = self.clock.tick() * 2 / 1000
            self.period.text = str(timeSpan)
            self.angularVelocity.text = str(2 * pi / (1 if timeSpan == 0 else timeSpan))

        self.offset += vec2d(1, 0)
        surface.blit(self.graph, (-self.offset[0], 0))

    def draw(self, surface: pygame.surface.Surface):
        return super().draw(surface)

    def handleSetting(self) -> None:
        mass = self.massTextBox.getContent(float, 1)
        mass = max(mass, 0.00000000000001)
        self.singleParticle.mainParticle.mass = Kilogram(mass)

        if self.resetAmpBox.activated:
            self.max = -9999999999
            self.min = 99999999999
            self.amplitudeText.text = ''

        return super().handleSetting()
        