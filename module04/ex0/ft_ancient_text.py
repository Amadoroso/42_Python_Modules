
import sys
import typing


def main() -> None:

    if len(sys.argv) != 2:
        print("Usage: python3 ft_ancient_text.py <file>")
        return
    file: typing.IO | None = None
    try:
        print(f"""=== Cyber Archives Recovery ===
Accessing file '{sys.argv[1]}'""")
        file = open(sys.argv[1], "r")
        print(f"---\n\n{file.read()}\n---")
        print(f"File '{sys.argv[1]}' closed.")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except IsADirectoryError as e:
        print(f"'{sys.argv[1]}' is a directory: {e}")
    finally:
        if file:
            file.close()


if __name__ == "__main__":
    main()
