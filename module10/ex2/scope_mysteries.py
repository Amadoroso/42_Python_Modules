
from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:

    count: int = 0

    def call_counter() -> int:
        nonlocal count
        count += 1
        return count

    return call_counter


def spell_accumulator(initial_power: int) -> Callable:

    def power_acc(power_to_add: int) -> int:
        nonlocal initial_power
        initial_power += power_to_add
        return initial_power

    return power_acc


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchant_applier(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant_applier


def memory_vault() -> dict[str, Callable]:

    persistant_dict: dict[Any, Any] = {}

    def store(key: Any, value: Any) -> None:
        persistant_dict[key] = value

    def recall(key: Any) -> Any:
        try:
            return persistant_dict[key]
        except KeyError:
            return "Memory not found"

    return {
        "store": store,
        "recall": recall
        }


def main() -> None:

    print("Testing mage counter...")
    counter_a, counter_b = mage_counter(), mage_counter()
    for x in range(1, 3):
        print(f"counter_a call {x}: {counter_a()}")
        print(f"counter_b call {x}: {counter_b()}")
    print()

    print("Testing spell accumulator...")
    acc: Callable = spell_accumulator(100)
    print(f"Base 100, adding 20: {acc(20)}")
    print(f"Base 100, adding 30: {acc(30)}")
    print()

    print("Testing enchantment factory...")
    factory: Callable = enchantment_factory("Flaming")
    print(f"{factory('sword')}")
    print(f"{factory('shield')}")
    print()

    print("Testing memory vault...")
    func_dict: dict[str, Callable] = memory_vault()
    print("Store 'secret' = 42")
    func_dict['store']('secret', 42)
    print(f"Recall 'secret' = {func_dict['recall']('secret')}")
    print(f"Recall 'unknown' = {func_dict['recall']('unknown')}")
    print()


if __name__ == "__main__":
    main()
