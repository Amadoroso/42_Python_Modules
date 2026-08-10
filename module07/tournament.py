
import random
from ex0 import FlameFactory, AquaFactory, CreatureFactory, Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy,
    AgressiveStrategy,
    DefensiveStrategy,
    BattleStrategy,
    InvalidCreature,
    Colors
)


def factory_creator() -> list[CreatureFactory]:
    return [
        FlameFactory(),
        AquaFactory(),
        HealingCreatureFactory(),
        TransformCreatureFactory()
    ]


def strategy_creator() -> list[BattleStrategy]:
    return [
        NormalStrategy(),
        AgressiveStrategy(),
        DefensiveStrategy()
    ]


def random_opp(
        factories: list[CreatureFactory],
        strategies: list[BattleStrategy]
        ) -> list[tuple[CreatureFactory, BattleStrategy]]:

    opps: list[tuple[CreatureFactory, BattleStrategy]] = []
    opp_range: range = range(random.randrange(2, 5))
    for x in opp_range:
        opps.append((random.choice(factories), random.choice(strategies)))
    return opps


def battle(opp_lst: list[tuple[CreatureFactory, BattleStrategy]]) -> None:

    print(f"{len(opp_lst)} Opponents Involved!")
    creat_lst: list[tuple[Creature, BattleStrategy]] = []
    for fact, strat in opp_lst:
        evolved: bool = random.choice([True, False])
        if evolved:
            creat: Creature = fact.create_evolved()
        else:
            creat = fact.create_base()
        creat_lst.append((creat, strat))

    count: int = 1
    for i in range(len(creat_lst)):
        for j in range(i + 1, len(creat_lst)):
            creat1 = creat_lst[i]
            creat2 = creat_lst[j]
            print(f"==== BATTLE {count} ====")
            print(f"{creat1[0].describe()} + \
{creat1[1]}\nVS\n{creat2[0].describe()} + {creat2[1]}")
            count = count + 1
            print("==== Now FIGHT ====")
            for creat_tup in (creat1, creat2):
                try:
                    creat_tup[1].act(creat_tup[0])
                except InvalidCreature as e:
                    err: str = e.__str__()
                    print(err.replace("[CREATURE]", creat_tup[0].name))
                    print("Aborting Tournament...")
                    print()
                    return


def main() -> None:

    factories: list[CreatureFactory] = factory_creator()
    strategies: list[BattleStrategy] = strategy_creator()

    for tournament in range(0, 5):
        print(f"{Colors.GREEN}==== Tournament {tournament} ===={Colors.END}")
        battle(random_opp(factories, strategies))


if __name__ == "__main__":
    main()
