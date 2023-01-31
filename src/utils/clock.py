from pygame.time import Clock


class ClockLoader:

    _clock: Clock = Clock()

    @classmethod
    @property
    def clock(cls) -> Clock:
        return cls._clock
