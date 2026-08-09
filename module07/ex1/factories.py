
from ex0 import CreatureFactory
from .new_creatures import Sproutling, Bloomelle, Shiftling, Morphagon


# ------------ Healers
class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


# ---------------- Transformers
class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
