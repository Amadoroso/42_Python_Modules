
def secure_archive(file_name: str, action: str = "r",
                   content: str = "") -> tuple[bool, str]:

    try:
        if action == "w":
            with open(file_name, action) as file:
                file.write(content)
                return (True, content)
        elif action == "r" and content:
            return (False, "'r' flag doens't need content")
        elif action == "r" and not content:
            with open(file_name, action) as file:
                return (True, file.read())
        else:
            return (False, f"Invalid '{action}' flag")

    except FileNotFoundError as e:
        return (False, e.__str__())
    except PermissionError as e:
        return (False, e.__str__())
    except IsADirectoryError as e:
        return (False, e.__str__())


def main() -> None:

    print("=== Cyber Archives Security ===")
    print("\nUsing 'secure_archive() to read non existent file:")
    print(secure_archive("abc", "r"))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/sudoers", "r"))
    print("\nUsing 'secure_archive' to read from normal file:")
    print(secure_archive("a", "r"))
    print("\nUsing 'secure_archive' to write to a new file:")
    print(secure_archive("new", "w", "new content for the new file\n"))
    print("\nUsing 'secure_archive' to write to a new file \
(with the 'r' flag):")
    print(secure_archive("new_file", "r", "new content for the new file\n"))
    print("\nUsing 'secure_archive' to write to a new file (with no content):")
    print(secure_archive("new_file", "w"))
    print("\nUsing 'secure_archive'  without passing an action nor content:")
    print(secure_archive("a"))


if __name__ == "__main__":
    main()
