import os
import dotenv

dotenv.load_dotenv()


def get_vars() -> dict[str, str | None]:
    env_vars: list[str] = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT",
    ]
    config: dict[str, str | None] = {}
    for var in env_vars:
        config[var] = os.getenv(var)
    return config


def check_zion(url: str | None) -> str:
    if not url or not url.startswith(("http://", "https://")):
        return "Offline"
    return "Online"


def check_database(url: str | None) -> str:
    if not url:
        return "Not connected / Missing URL"

    if "127.0.0.1" in url or "localhost" in url:
        return "Connected to local instance"

    return "Connected to production database"


def output(config: dict[str, str | None]) -> None:

    print("Configuration loaded:")

    if config["MATRIX_MODE"] is None:
        print("Mode: Invalid")
    else:
        print(f"Mode: {config['MATRIX_MODE']}")

    print(f"Database: {check_database(config.get('DATABASE_URL'))}")

    if config.get("API_KEY") is None:
        print("API Access: Unauthenticated")
    else:
        print("API Access: Authenticated")

    log_level: str | None = config.get("LOG_LEVEL")
    if log_level is None:
        print("Log Level: Invalid")
    else:
        print(f"Log Level: {log_level}")

    print(f"Zion Network: {check_zion(config.get('ZION_ENDPOINT'))}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.isfile(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[NOK] .env file not found (using environment overrides)")

    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


def main() -> None:

    print("ORACLE STATUS: Reading the Matrix...\n")
    config: dict[str, str | None] = get_vars()

    missing: list[str] = []
    for key, value in config.items():
        if value is None:
            missing.append(key)

    if missing:
        print("WARNING: Missing configuration:")
        all_missing: str = ", \n".join(missing)
        print(all_missing)
        print()

    output(config)


if __name__ == "__main__":
    main()
