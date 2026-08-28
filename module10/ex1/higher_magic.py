
from typing import Callable
import random as rd


# Spells
class Spells():

    @staticmethod
    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    @staticmethod
    def fireball(target: str, power: int) -> str:
        return f"Fireball burns {target} for {power} HP"


# Functions that take spells as arguments
def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    def amp_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amp_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda target, power: spell(target, power) \
        if not condition(target, power) else "Spell fizzled"


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target, power: [spell(target, power) for spell in spells]


def main() -> None:

    # Higher Realm Test Data
    # Use these in your test functions:
    test_power_val = [12, 9, 24]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    print("Testing spells individually:")
    print(Spells.heal(rd.choice(test_targets), rd.choice(test_power_val)))
    print(Spells.fireball(rd.choice(test_targets), rd.choice(test_power_val)))
    print()

    print("Testing spell_combiner():")
    combined: Callable = spell_combiner(Spells.heal, Spells.fireball)
    out1, out2 = combined(rd.choice(test_targets), rd.choice(test_power_val))
    print(f"{out1}, {out2}")
    print()

    print("Testing power_amplifier():")
    amper: Callable = power_amplifier(Spells.heal, 4)
    print(f"Base Heal: {Spells.heal('Dragon', 12)}")
    print(f"Amp heal: {amper('Dragon', 12)}")
    print()

    print("Testing conditional_caster():")
    power_check: Callable = lambda target, power: True \
        if power >= 10 else False
    cond_heal: Callable = conditional_caster(power_check, Spells.heal)
    print(cond_heal(rd.choice(test_targets), rd.choice(test_power_val)))
    print()

    print("Testing spell_sequence():")
    seq: Callable = spell_sequence([Spells.heal, Spells.fireball])
    print(seq(rd.choice(test_targets), rd.choice(test_power_val)))


if __name__ == "__main__":
    main()
