
import alchemy


if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Using: 'import alchemy' to access the alchemy package")
    print(f"Testing create_air(): {alchemy.create_air()}")
    print("Testing create_earth(), which will raise an expcetion: ", end=" ")
    try:
        alchemy.create_earth()  # type: ignore
    except AttributeError as e:
        print(f"{e}")
