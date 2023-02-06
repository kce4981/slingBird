

class Kilogram:

    _value: float

    def __init__(self, value:float) -> None:
        self.value = value

    def from_gram(self, value):
        self.value = value / 1000 

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v