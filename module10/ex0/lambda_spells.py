
class Data():

    # Generated Lambda Sanctum Test Data
    artifacts: list[dict] = [
        {
            'name': 'Ice Wand',
            'power': 95,
            'type': 'armor'
        },
        {
            'name': 'Lightning Rod',
            'power': 98,
            'type': 'focus'
        },
        {
            'name': 'Wind Cloak',
            'power': 86,
            'type': 'focus'
        },
        {
            'name': 'Ice Wand',
            'power': 69,
            'type': 'weapon'
        }
    ]

    mages: list[dict] = [
        {
            'name': 'Phoenix',
            'power': 99,
            'element': 'wind'
        },
        {
            'name': 'River',
            'power': 58,
            'element': 'lightning'
        },
        {
            'name': 'Sage',
            'power': 84,
            'element': 'water'
        },
        {
            'name': 'Phoenix',
            'power': 88,
            'element': 'water'
        },
        {
            'name': 'Storm',
            'power': 68,
            'element': 'shadow'
        }
    ]

    spells: list[str] = [
        'tornado',
        'shield',
        'meteor',
        'heal'
    ]


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact['power'],
        reverse=True
        )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:

    power_list: list[int] = list(map(lambda mage: mage['power'], mages))
    return {
        'max_power': max(mages, key=lambda mage: mage['power'])['power'],
        'min_power': min(mages, key=lambda mage: mage['power'])['power'],
        'avg_power': round(sum(power_list)/len(power_list), 2)
    }


def main() -> None:

    print("Testing artifact_sorter(): ")
    print(f"Original artifact list order: \n\
{[artifact['name'] for artifact in Data.artifacts]}")
    print(f"After sorting artifacts according to their power (descebing): \n\
{[artifact['name'] for artifact in artifact_sorter(Data.artifacts)]}")
    print()
    print("Testing power_filter(): ")
    print(f"Full mage list: \n {[mage['name'] for mage in Data.mages]}")
    print(f"Filtered mages by min_power=75: \n\
{[mage['name'] for mage in power_filter(Data.mages, 75)]}")
    print()
    print("Testing spell_transformer(): ")
    print(f"Spell list: \n {Data.spells}")
    print(f"Modded spell list: \n {spell_transformer(Data.spells)}")
    print()
    print("Testing mage_stats(): ")
    print(mage_stats(Data.mages))


if __name__ == "__main__":
    main()
