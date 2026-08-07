
from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:

    for x in dark_spell_allowed_ingredients():
        if x in ingredients.lower():
            return ingredients + " VALID"
    return ingredients + " INVALID"
