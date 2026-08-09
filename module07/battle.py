
from ex0 import FlameFactory, AquaFactory, CreatureFactory, Creature


def validate(factory: CreatureFactory) -> bool:

    print(f"Testing {factory.__class__.__name__}:")
    try:
        base: Creature = factory.create_base()
        print(base.describe())
        print(base.attack())
        evolved: Creature = factory.create_evolved()
        print(evolved.describe())
        print(evolved.attack())
        print()
    except AttributeError as e:
        print(f"Caught bad {factory}: {e}")
        print(f"{factory} will be removed!")
        return False
    return True


def battle(factory_lst: list[CreatureFactory]) -> None:

    print("Testing battle...")
    if len(factory_lst) < 2 or len(factory_lst) % 2 != 0:
        print("Not enough Creatures to battle :/")
        return

    for factory1, factory2 in zip(factory_lst[::2], factory_lst[1::2]):
        print(factory1.create_base().describe())
        print("vs")
        print(factory2.create_base().describe())
        print("fight!")
        print(factory1.create_base().attack())
        print(factory2.create_base().attack())


def main() -> None:

    factory_lst: list[CreatureFactory] = [
        FlameFactory(),
        AquaFactory()
    ]

    for factory in factory_lst:
        if not validate(factory):
            factory_lst.remove(factory)
    battle(factory_lst)


if __name__ == "__main__":
    main()
