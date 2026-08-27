
from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from typing import Optional
from datetime import datetime


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validation(self) -> 'AlienContact':

        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID \
doesn't start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical \
contact reports must be verified")
        if self.contact_type == ContactType.TELEPATHIC and \
                self.witness_count < 3:
            raise ValueError("Telephatic \
contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals \
(> 7.0) should include received message")

        return self

    def __str__(self) -> str:

        return f"""
ID: {self.contact_id}
Type: {self.contact_type.value}
Location: {self.location}
Signal: {self.signal_strength}/10
Duration: {self.duration_minutes} minutes
Witnesses: {self.witness_count}
Message: '{self.message_received}'"""


def main() -> None:

    print("Alien Contact Log Validation")
    print("============================")
    try:
        print("Valid contact report:")
        valid: AlienContact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            contact_type="radio",  # type: ignore
            location="Area 51, Nevada",
            signal_strength="8.5",  # type: ignore
            duration_minutes="45",  # type: ignore
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print(valid, end='\n\n')
        print("============================")
        print("Invalid contact report:\n")
        invalid: AlienContact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            contact_type=ContactType.TELEPATHIC,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli"
        )
        print(invalid)
    except ValidationError as e:
        print("Caught Validation Error:")
        for errors in e.errors():
            print(errors['msg'].replace(',', ':'))


if __name__ == "__main__":
    main()
