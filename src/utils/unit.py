

class Kilogram:

    value: float

    def __init__(self, value:float) -> None:
        self.value = value

    def from_gram(self, value):
        self.value =  value / 1000 

    def getValue(self):
        return self.value