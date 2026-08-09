
from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
    Healers,
    Transformers
)


def main() -> None:

    print("Testing Creature with healing capability")
    print("base:")
    healer: Healers = HealingCreatureFactory().create_base()
    print(healer.describe())
    print(healer.attack())
    print(healer.heal())
    print("Evolved:")
    healer = HealingCreatureFactory().create_evolved()
    print(healer.describe())
    print(healer.attack())
    print(healer.heal())
    print("Evolved:")
    print()
    transformer: Transformers = TransformCreatureFactory().create_base()
    print(transformer.describe())
    print(transformer.attack())
    print(transformer.transform())
    print(transformer.attack())
    print(transformer.revert())
    print("Evolved:")
    transformer = TransformCreatureFactory().create_evolved()
    print(transformer.describe())
    print(transformer.attack())
    print(transformer.transform())
    print(transformer.attack())
    print(transformer.revert())


if __name__ == "__main__":
    main()
