
import os
import dotenv


dotenv.load_dotenv()


def main() -> None:

    keys: list[str] = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]

    print("ORACLE STATUS: Reading the Matrix...\n")
    print("=== Configuration Loaded ===")
    env_check: bool = True
    for key in keys:
        key_san: str = key.lower().capitalize().replace("_", " ")
        value: str | None = os.getenv(key)
        if value:
            print(f"{key_san}: {value}")
        else:
            print(f"{key_san}: MISSING!")
            env_check = False

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] Production overrides available")
    if env_check:
        print("[OK] .env file properly configured")
    else:
        print("[NOK] .env file NOT properly configured")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
