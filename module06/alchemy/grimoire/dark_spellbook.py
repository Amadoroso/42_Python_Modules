
from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:

    if "VALID" in dark_validate_ingredients(ingredients):
        return "Spell was recorded"
    else:
        return "Spell was rejected"
