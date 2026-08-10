
from abc import ABC, abstractmethod
from ex0 import Creature
from ex1 import Transformers, Healers
from .colors import Colors
from typing import cast


class InvalidCreature(Exception):

    def __init__(self, message="") -> None:
        self.message = message

    def __str__(self) -> str:

        base: str = f"{Colors.RED}\
Invalid Creature for this strategy{Colors.END}"
        if self.message:
            return base + ": " + self.message
        else:
            return base


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    def __str__(self) -> str:
        return self.__class__.__name__


class NormalStrategy(BattleStrategy):

    def act(self, creature: Creature) -> None:

        if self.is_valid(creature):
            print(creature.attack())
        else:
            raise InvalidCreature

    def is_valid(self, creature: Creature) -> bool:

        try:
            creature.attack()
        except AttributeError:
            return False
        return True


class AgressiveStrategy(BattleStrategy):

    def act(self, creature: Creature) -> None:

        if self.is_valid(creature):
            creature = cast(Transformers, creature)
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        else:
            raise InvalidCreature("[CREATURE] \
must have Transforming Capabilities")

    def is_valid(self, creature: Creature) -> bool:

        try:
            creature = cast(Transformers, creature)
            creature.attack()
            creature.transform()
            creature.revert()
        except AttributeError:
            return False
        return True


class DefensiveStrategy(BattleStrategy):

    def act(self, creature: Creature) -> None:

        if self.is_valid(creature):
            creature = cast(Healers, creature)
            print(creature.attack())
            print(creature.heal())
        else:
            raise InvalidCreature("[CREATURE] \
must have Healing Capabilities")

    def is_valid(self, creature: Creature) -> bool:

        try:
            creature = cast(Healers, creature)
            creature.attack()
            creature.heal()
        except AttributeError:
            return False
        return True
