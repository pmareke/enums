from enum import Enum, unique

from dataclasses import dataclass


@unique
class EngineerType(Enum):
    JUNIOR = "Junior"
    SENIOR = "Senior"
    STAFF = "Staff"
    TEAM_LEAD = "Team Lead"
    ENGINEERING_MANAGER = "Engineering Manager"

    @staticmethod
    def all_values() -> list[str]:
        return [item.value for item in list(EngineerType)]

    @staticmethod
    def from_(value: str) -> "EngineerType":
        try:
            return EngineerType(value)
        except ValueError as ex:
            raise InvalidEngineeringTypeException(value) from ex


@dataclass
class Engineer:
    name: str
    salary: int
    type: EngineerType


class InvalidEngineeringTypeException(Exception):
    def __init__(self, invalid_type: str) -> None:
        error_message = f"Sorry the type '{invalid_type}' is not correct, please use one of {EngineerType.all_values()}"
        super().__init__(error_message)
