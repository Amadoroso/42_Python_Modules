
if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Using 'from alchemy.grimoire import dark_spellbook' directly")
    print("THIS WILL RAISE AN EXCEPTION DUE TO A CIRCULAR IMPORT")
    try:
        from alchemy.grimoire import dark_spellbook
        print("Testing record light spell: ")
        print(dark_spellbook.dark_spell_record(
            'Fantasy',
            'Earth, wind and fire'
            )
        )
    except ImportError as e:
        print(f"{e}")
