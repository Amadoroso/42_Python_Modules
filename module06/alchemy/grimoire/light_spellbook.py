
def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:

    from .light_validator import validate_ingredients
    output: str = validate_ingredients(ingredients)

    if "VALID" in output:
        return "Spell was recorded: " + output
    else:
        return "Spell was rejected: " + output
