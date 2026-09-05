
from typing import Any
from collections.abc import Callable
import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:

    ops: dict[str, Callable] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    try:
        ops[operation]
        return functools.reduce(ops[operation], spells)
    except KeyError:
        return 0


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:

    return {
        "fire": functools.partial(
            base_enchantment,
            power=50,
            element="fire"
            ),
        "water": functools.partial(
            base_enchantment,
            power=50,
            element="water"
            ),
        "wind": functools.partial(
            base_enchantment,
            power=50,
            element="wind"
            )
        }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n in (0, 1):
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @functools.singledispatch
    def spell(spell: Any) -> str:
        return "Unknown Spell Type"

    @spell.register
    def dmg_spell(amount: int) -> str:
        return f"Damage Spell: {amount} damage"

    @spell.register
    def enchantment(name: str) -> str:
        return f"Enchantment: {name}"

    @spell.register
    def multi_cast(multi: list) -> str:
        return f"Multi-cast: {len(multi)} spells"

    return spell


def main() -> None:

    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer([10, 50, 20, 35], 'add')}")
    print(f"Product: {spell_reducer([10, 50, 20, 35], 'multiply')}")
    print(f"Max: {spell_reducer([10, 50, 20, 35], 'max')}")
    print(f"Min: {spell_reducer([10, 50, 20, 35], 'min')}")
    print()

    print("Testing Partial Enchanter...")
    partials: dict[str, Callable] = partial_enchanter(
        lambda power, element, target:
            f"{element} with {power} was thrown to {target}"
        )
    for n, key in enumerate(partials):
        print(f"Partial function {n}: {partials[key](target='cat')}")
    print()

    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Fib(500): {memoized_fibonacci(500)}")
    print(f"Fib(500) 2nd time: {memoized_fibonacci(500)}")
    print("The second time is faster because the result is cached")
    print()

    print("Testing spell dispatcher...")
    dispatcher_function: Callable = spell_dispatcher()
    print(dispatcher_function(42))
    print(dispatcher_function("firebal"))
    print(dispatcher_function([42, "fireball", 100]))
    print(dispatcher_function({
        "andre": 2
    }))


if __name__ == "__main__":
    main()
