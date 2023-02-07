from pygame.math import Vector2
from enum import Enum

vec2d = Vector2

#class vec2d(Vector2):
#    pass

class Face(Enum):

    UP = vec2d(0, -1)
    DOWN = vec2d(0, 1)
    LEFT = vec2d(-1, 0)
    RIGHT = vec2d(1, 0)

    @classmethod
    def getReverse(cls, face: 'Face'):
        match face:
            case cls.UP:
                return cls.DOWN
            case cls.DOWN:
                return cls.UP
            case cls.LEFT:
                return cls.RIGHT
            case cls.RIGHT:
                return cls.LEFT