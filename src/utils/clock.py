from pygame.time import Clock
from .config import ConfigLoader


class ClockLoader:

    _clock: Clock = Clock()

    @classmethod
    @property
    def clock(cls) -> Clock:
        return cls._clock

    @classmethod
    def getTime(cls) -> float:
        "returns second"
        # get_time() returns millisecond
        return cls.clock.get_time() / 1000 * ConfigLoader.speed
