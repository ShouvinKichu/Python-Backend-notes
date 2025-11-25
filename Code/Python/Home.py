class SuperHero():

    def __init__(self, name: str, level: int, power: str):
        self.name = name
        self._level = level
        self.power = power

    @property
    def level(self) -> int:
        return self._level
    
    def activate(self) -> None:
        print(f"{self.name} has activated {self.power}")


spidy = SuperHero("Spiderman", 3, "spidysense")
print(spidy.name)
print(spidy.level)
spidy.activate()