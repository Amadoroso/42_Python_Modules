

import sys
print("\nLOADING STATUS: Loading programs...")
print("\nChecking dependencies:")
try:
    import requests
    print(f"[OK] {requests.__name__} ({requests.__version__})")
    import pandas
    print(f"[OK] {pandas.__name__} ({pandas.__version__})")
    import numpy
    print(f"[OK] {numpy.__name__} ({numpy.__version__})")
    import matplotlib
    import matplotlib.figure
    import matplotlib.axes
    import matplotlib.pyplot as pyplot
    print(f"[OK] {matplotlib.__name__} ({matplotlib.__version__})")
except ImportError as e:
    print(f"Missing dependency: {e}")
    print(f"Will stop checking!\n")
    print("=== Dependency instalation instructions ===\n")
    print("For pip:\n$ pip install -r requirements.txt")
    print("Make sure you're running inside a venv\n")
    print("For Poetry:\n$ poetry install\n")
    print("Aborting execution...")
    sys.exit(42)


def get_IPMA_data(
        id_endpoint: str,
        meteo_endpoint: str,
        city: str
        ) -> pandas.DataFrame:

    print("Retrieving IPMA district capital IDs...")
    district_json: dict = requests.get(id_endpoint).json()
    dist_data: list[dict] = district_json["data"]

    globIdLocal: str = ""
    for region in dist_data:
        if region["local"] == city:
            globIdLocal = str(region["globalIdLocal"])
    if not globIdLocal:
        print(f"\n'{city}' isn't in IPMAs database.")
        print("The program will abort.")
        return pandas.DataFrame()

    print(f"Retrieving {city}'s 5 day Temperature report...")
    full_meteo_endpoint = meteo_endpoint.replace('[ID]', globIdLocal)
    meteo_response: requests.Response = requests.get(full_meteo_endpoint)
    meteo_json: dict = meteo_response.json()
    meteo_data = meteo_json["data"]
    meteo_df: pandas.DataFrame = pandas.DataFrame(meteo_data)
    meteo_df = meteo_df[["forecastDate", "tMax", "tMin"]]
    meteo_df["tMax"] = meteo_df["tMax"].astype(float)

    return meteo_df.astype({"tMax": float, "tMin": float})


def plotter(data: pandas.DataFrame, city: str) -> None:

    print("Generating visualization...")
    fig: matplotlib.figure.Figure
    ax: matplotlib.axes.Axes
    fig, ax = pyplot.subplots()
    ax.plot(
        data["forecastDate"],
        data["tMin"],
        marker="o",
        linestyle="--",
        label="Min Temp",
        color="blue"
    )
    ax.plot(
        data["forecastDate"],
        data["tMax"],
        marker="o",
        linestyle="--",
        label="Max Temp",
        color="red"
    )
    ax.set_xlabel("Date")
    ax.set_ylabel("T (ºC)")
    ax.set_title(f"Previsão Meteorológica Diária \
até 5 dias: {city}")
    ax.legend()
    pyplot.show()


def main() -> None:

    city: str = input("\nPlease input a valid \
District capital Portuguese city (i.e: Lisboa): ")
    city = city.lower().capitalize().replace(" ", "")

    df: pandas.DataFrame = get_IPMA_data(
        "https://api.ipma.pt/open-data/distrits\
-islands.json",
        "https://api.ipma.pt/open-data/forecast\
/meteorology/cities/daily/[ID].json",
        city
        )
    if df.empty:
        return
    else:
        plotter(df, city)


if __name__ == "__main__":
    main()
