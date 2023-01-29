import pygame
from pygame.locals import *
from .scene import BaseScene

class SlingBird:

    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1280, 720))
        self.background = self.surface.copy()


    def run(self, scene: BaseScene, framerate):
        clock = pygame.time.Clock()

        running = True
        while(running):

            clock.tick(framerate)
            self.surface.blit(self.background, (0, 0))
            scene.draw(self.surface)
            pygame.display.flip()


            for event in pygame.event.get():
                if event == QUIT:
                    pygame.quit()
