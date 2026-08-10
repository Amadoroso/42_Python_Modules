
from abc import ABC, abstractmethod


class Creature(ABC):

    def __init__(self) -> None:
        self.name: str = "[CREATURE NAME]"
        self.type: str = "[CREATURE TYPE]"

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"

    def __str__(self) -> str:
        return self.__class__.__name__


class Flameling(Creature):

    def __init__(self) -> None:
        super().__init__()
        self.name: str = "Flameling"
        self.type: str = "Fire"

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):

    def __init__(self) -> None:
        super().__init__()
        self.name: str = "Pyrodon"
        self.type: str = "Fire/Flying"

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):

    def __init__(self) -> None:
        super().__init__()
        self.name: str = "Aquabub"
        self.type: str = "Water"

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):

    def __init__(self) -> None:
        super().__init__()
        self.name: str = "Torragon"
        self.type: str = "Water"

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"
