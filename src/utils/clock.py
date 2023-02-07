from pygame.time import Clock


class ClockLoader:

    _clock: Clock = Clock()

    @classmethod
    @property
    def clock(cls) -> Clock:
        return cls._clock

    @classmethod
    def getTime(cls) -> float:
        "return second"
        from . import ConfigLoader

        return cls._clock.get_time() * ConfigLoader.speed / 1000 # ms to sec