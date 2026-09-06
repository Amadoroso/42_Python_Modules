
from collections.abc import Callable
from typing import Any
import functools
import time


def spell_timer(func: Callable) -> Callable:

    @functools.wraps(func)  # keeping previous identity
    def wrapper(*args: Any, **kwords: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start: float = time.time()
        result: Any = func(*args, **kwords)
        end: float = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:

    def validator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(*args: Any, **kargs: Any) -> Any:
            if "power" in kargs:
                if kargs["power"] >= min_power:
                    return func(*args, **kargs)
                else:
                    return "Insufficient power for this spell"
            elif len(args) == 3:
                if args[2] >= min_power:  # Im assuming power is the third arg
                    return func(*args, **kargs)
                else:
                    return "Insufficient power for this spell"
            else:
                return "Invalid function signature"

        return wrapper

    return validator


def retry_spell(max_attempts: int) -> Callable:

    def validator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(*args: Any, **kwords: Any) -> Any:
            for n in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwords)
                except Exception:
                    if n < max_attempts:
                        print(f"Spell failed, retrying... \
(attempt {n}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return validator


class MageGuild:

    def __init__(self, name: str) -> None:
        if self.validate_mage_name(name):
            self.name = name
        else:
            print(f"'{name}' is invalid for a Mage")

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and name.isalnum():
            return True
        else:
            return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} \
with {power} power"


def main() -> None:

    print("Testing spell timer...")
    modded_spell_caster: Callable = spell_timer(
        lambda spell_name: f'{spell_name} cast!'
        )
    print(modded_spell_caster("fireball"))
    print()

    print("Testing retrying spell")

    @retry_spell(3)
    def spell(name: str):
        return f"{name} spelled!"
    print(spell())  # type: ignore
    print(spell("Waaaaaaag"))
    print()

    print("Testing MageGuild")
    mage1: MageGuild = MageGuild("Miguel")
    mage2: MageGuild = MageGuild("Mi")
    mage2.validate_mage_name("Mi")  # Para calar flake8
    print(f'{mage1.cast_spell("Lightning", power=15)}')
    print(f'{mage1.cast_spell("Fireball", power=5)}')


if __name__ == "__main__":
    main()
