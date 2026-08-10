
from ex0 import CreatureFactory
from .new_creatures import (
    Sproutling,
    Bloomelle,
    Shiftling,
    Morphagon,
    Healers,
    Transformers
)


# ------------ Healers
class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Healers:
        return Sproutling()

    def create_evolved(self) -> Healers:
        return Bloomelle()


# ---------------- Transformers
class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Transformers:
        return Shiftling()

    def create_evolved(self) -> Transformers:
        return Morphagon()
