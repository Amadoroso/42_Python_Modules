
from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=5)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validator(self) -> 'SpaceMission':

        cap_com: bool = False
        all_active: tuple[bool, str] = (True, "")
        year_exp: int = 0
        for member in self.crew:
            if member.rank in (Rank.COMMANDER, Rank.CAPTAIN):
                cap_com = True
            if member.years_experience >= 5:
                year_exp = year_exp + 1
            if not member.is_active:
                all_active = (False, member.name)

        if not self.mission_id.startswith("M"):
            raise ValueError("Invalid mission ID")

        if not cap_com:
            raise ValueError("At least one crew member must be \
a Commander or Captain")

        if self.duration_days > 365 and year_exp/len(self.crew) < 0.5:
            raise ValueError("For long missions (> 365 days), \
at least 50% of the crew must have 5+ years of experience")

        if not all_active[0]:
            raise ValueError(f"{all_active[1]} isn't active, \
all crew members must be active")

        return self

    def __str__(self) -> str:

        crew_members: str = ""
        for member in self.crew:
            crew_members = crew_members \
                + f"- {member.name} ({member.rank.value}) - \
{member.specialization}\n"

        return f"""
Mission: {self.mission_name}
ID: {self.mission_id}
Destination: {self.destination}
Duration: {self.duration_days} days
Budget: ${self.budget_millions}M
Crew size: {len(self.crew)}
Crew members:\n""" + crew_members


def demo() -> None:

    print("Space Mission Crew Validation")
    print("=============================")
    try:
        print("Valid mission created:")
        valid: SpaceMission = SpaceMission(
            mission_name="Mars Colony Establishment",
            mission_id="M2024_MARS",
            destination="Mars",
            duration_days=900,
            budget_millions=2500.0,
            launch_date=datetime.now(),
            crew=[
                CrewMember(
                    member_id="123",
                    name="Sarah Connor",
                    rank=Rank.COMMANDER,
                    age=20,
                    specialization="Mission Command",
                    years_experience=6,
                    is_active=True
                ),
                CrewMember(
                    member_id="456",
                    name="john Smith",
                    rank=Rank.LIEUTENANT,
                    age=21,
                    specialization="Navigation",
                    years_experience=6,
                    is_active=True
                ),
                CrewMember(
                    member_id="789",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=22,
                    specialization="Engineering",
                    years_experience=9,
                    is_active=True
                )
            ]
        )
        print(valid)
        print("=============================")
        print("Invalid mission created:")
        invalid: SpaceMission = SpaceMission(
            mission_name="Mars Colony Establishment",
            mission_id="M2024_MARS",
            destination="Mars",
            duration_days=900,
            budget_millions=2500.0,
            launch_date=datetime.now(),
            crew=[
                CrewMember(
                    member_id="123",
                    name="Sarah Connor",
                    rank=Rank.CADET,
                    age=20,
                    specialization="Mission Command",
                    years_experience=6,
                    is_active=True
                ),
                CrewMember(
                    member_id="456",
                    name="john Smith",
                    rank=Rank.LIEUTENANT,
                    age=21,
                    specialization="Navigation",
                    years_experience=6,
                    is_active=True
                ),
                CrewMember(
                    member_id="789",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=22,
                    specialization="Engineering",
                    years_experience=9,
                    is_active=True
                )
            ]
        )
        print(invalid)
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg']}")


if __name__ == "__main__":
    demo()
