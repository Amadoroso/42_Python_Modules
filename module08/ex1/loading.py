
import sys

try:
    import requests
    import pandas
    import numpy
    import matplotlib
    import matplotlib.figure
    import matplotlib.axes
    import matplotlib.pyplot as pyplot
except ImportError:
    pass


def check_dependencies() -> bool:

    all_loaded: bool = True
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    packages: dict[str, str] = {
        "requests": "Network access ready",
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready"
    }
    for name, description in packages.items():
        if name in sys.modules:
            print(f"[OK] {name} ({sys.modules[name].__version__}) \
- {description}")
        else:
            print(f"[NOK] {name} - not installed!")
            all_loaded = False

    print()
    return all_loaded


def gen_wind_speed(meteo_df: "pandas.DataFrame") -> "pandas.DataFrame":

    random_wspeed: "numpy.ndarray" = numpy.random.uniform(
        100,
        200,
        len(meteo_df)
        )
    meteo_df["Top Wind Speed"] = numpy.round(random_wspeed, 1)
    print("\n==== Using Numpy to generate data ====")
    print("Generating random 'Top Wind Speeds' using numpy")
    return meteo_df


def get_IPMA_data(
        id_endpoint: str,
        meteo_endpoint: str,
        city: str
        ) -> "pandas.DataFrame":

    print("\n==== Using Get request to pull Weather info ====")
    print("Retrieving IPMA district capital IDs...")

    try:
        district_json: dict = requests.get(id_endpoint).json()
    except requests.exceptions.RequestException:
        return pandas.DataFrame()

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

    try:
        meteo_response: requests.Response = requests.get(full_meteo_endpoint)
    except requests.exceptions.RequestException:
        return pandas.DataFrame()

    meteo_json: dict = meteo_response.json()
    meteo_data = meteo_json["data"]
    meteo_df: "pandas.DataFrame" = pandas.DataFrame(meteo_data)
    meteo_df = meteo_df[["forecastDate", "tMax", "tMin"]]
    meteo_df["tMax"] = meteo_df["tMax"].astype(float)
    meteo_df = gen_wind_speed(meteo_df)

    return meteo_df.astype({"tMax": float, "tMin": float})


def plotter(data: "pandas.DataFrame", city: str) -> None:

    print("\nGenerating visualization...")
    fig: "matplotlib.figure.Figure"
    ax: "matplotlib.axes.Axes"
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
    ax2 = ax.twinx()
    ax2.plot(
        data["forecastDate"],
        data["Top Wind Speed"],
        marker="*",
        linestyle=":",
        label="Top Wind Speed",
        color="green"
    )
    ax.set_xlabel("Date")
    ax.set_ylabel("T (ºC)")
    ax2.set_ylabel("Top Wind Speed (Km/h)")
    ax.set_title(f"Previsão Meteorológica Diária \
até 5 dias: {city}")
    ax2.legend(loc="upper right")
    ax.legend(loc="lower right")
    pyplot.savefig('matrix_analysis.png')
    pyplot.show()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:

    if not check_dependencies():
        print("Missing modules!")
        print("=== Dependency installation instructions ===\n")
        print("For pip:\n$ pip install -r requirements.txt")
        print("Make sure you're running inside a venv\n")
        print("For Poetry:\n$ poetry install\n")
        print("Aborting execution...")
        sys.exit(42)
        return

    city: str = input("\nPlease input a valid \
District capital Portuguese city (i.e: Lisboa): ")
    city = " ".join(word.capitalize() for word in city.strip().split())

    df: pandas.DataFrame = get_IPMA_data(
        "https://api.ipma.pt/open-data/distrits\
-islands.json",
        "https://api.ipma.pt/open-data/forecast\
/meteorology/cities/daily/[ID].json",
        city
        )
    if df.empty:
        print("IPMA API not returning data -> Can't produce plot :(")
        return
    else:
        plotter(df, city)


if __name__ == "__main__":
    main()
