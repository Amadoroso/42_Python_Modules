
import sys
import typing


def reading_file() -> str:

    file: typing.IO | None = None
    try:
        print(f"""=== Cyber Archives Recovery ===
Accessing file '{sys.argv[1]}'""")
        file = open(sys.argv[1], "r")
        content: str = file.read()
        print(f"---\n\n{content}\n---")
        print(f"File '{sys.argv[1]}' closed.\n")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return ""
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return ""
    except IsADirectoryError as e:
        print(f"'{sys.argv[1]}' is a directory: {e}")
        return ""
    finally:
        if file:
            file.close()
    return content


def new_file(content: str) -> None:

    out_file: typing.IO | None = None
    try:
        print("Transform data:")
        content = content.replace('\n', '#\n')
        if content and not content.endswith('\n'):
            content = content + "#"
        print(f"---\n\n{content}\n---")
        new_name: str = input("Enter new file name (or leave empy): ")
        if not new_name:
            print("Not saving data")
            return
        print(f"Saving data to '{new_name}'")
        out_file = open(new_name, "w")
        out_file.write(content)
        print(f"Data saved to '{new_name}'")
    except FileNotFoundError as e:
        print(f"Error saving to file '{new_name}': {e}")
    except PermissionError as e:
        print(f"Error saving to file '{new_name}': {e}")
    except IsADirectoryError as e:
        print(f"'{new_name}' is a directory: {e}")
    finally:
        if out_file:
            out_file.close()


def main() -> None:

    if len(sys.argv) != 2:
        print("Usage: python3 ft_archive_creation.py <file>")
        return
    content: str = reading_file()
    if not content:
        return
    new_file(content)


if __name__ == "__main__":
    main()
