from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)

    def __str__(self) -> str:

        status: str = "Not Operational"
        if self.is_operational:
            status = "Operational"

        return f"""ID: {self.station_id}
Name: {self.name}
Crew {self.crew_size} people
Power: {self.power_level}%
Oxygen: {self.oxygen_level}%
last maintenance: {self.last_maintenance}
Status: {status}
Notes: {self.notes}"""


def main() -> None:

    print("Space Station Data Validation")
    print("==============================")
    try:
        print("Valid station created:")
        valid_ss: SpaceStation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            last_maintenance=datetime.now(),
            oxygen_level=92.3,
            is_operational=True
        )
        print(valid_ss)
        print("==============================")
        print("Expected Validation error:")
        invalid_ss: SpaceStation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=22,
            power_level=85.5,
            last_maintenance=datetime.now(),
            oxygen_level=92.3,
            is_operational=True
        )
        print(invalid_ss)
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'])


if __name__ == "__main__":
    main()
