
from .capabilities import HealCapability, TransformCapability
from ex0 import Creature
from abc import ABC


# ------------ Healers
class Healers(Creature, HealCapability, ABC):
    ...


class Sproutling(Healers):

    def __init__(self) -> None:
        Creature.__init__(self)
        HealCapability.__init__(self)
        self.name = "Sproutling"
        self.type = "Grass"

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Healers):

    def __init__(self) -> None:
        Creature.__init__(self)
        HealCapability.__init__(self)
        self.name = "Bloomelle"
        self.type = "Grass/Fairy "

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


# ---------------- Transformers
class Transformers(Creature, TransformCapability, ABC):
    ...


class Shiftling(Transformers):

    def __init__(self) -> None:
        Creature.__init__(self)
        TransformCapability.__init__(self)
        self.name = "Shiftling"
        self.type = "Normal"

    def attack(self) -> str:

        if self.transformed:
            return f"{self.name} performs a boosted strike!"
        else:
            return f"{self.name} attacks normally."

    def transform(self) -> str:

        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:

        if self.transformed:
            return f"{self.name} returns to normal."
        else:
            return f"{self.name} hasn't transformed yet!"


class Morphagon(Transformers):

    def __init__(self) -> None:
        Creature.__init__(self)
        TransformCapability.__init__(self)
        self.name = "Morphagon"
        self.type = "Normal/Dragon"

    def attack(self) -> str:

        if self.transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        else:
            return f"{self.name} attacks normally."

    def transform(self) -> str:

        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:

        if self.transformed:
            return f"{self.name} stabilizes its form."
        else:
            return f"{self.name} hasn't transformed yet!"
