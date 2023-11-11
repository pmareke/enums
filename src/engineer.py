from enum import Enum, unique

from dataclasses import dataclass


@unique
class EngineerType(Enum):
    JUNIOR = "Junior"
    SENIOR = "Senior"
    STAFF = "Staff"
    TEAM_LEAD = "Team Lead"
    ENGINEERING_MANAGER = "Engineering Manager"

    def is_junior(self) -> bool:
        return self == self.JUNIOR

    @staticmethod
    def all_values() -> list[str]:
        return [item.value for item in list(EngineerType)]


@dataclass
class Engineer:
    name: str
    salary: int
    type: EngineerType
