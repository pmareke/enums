import pytest

from expects import equal, expect, raise_error

from src.enums import calculate_engineer_cost
from src.engineer import Engineer, EngineerType, InvalidEngineeringTypeException


class TestEnums:
    @pytest.mark.parametrize(
        "engineer_type,salary,expected_total_cost",
        [
            (EngineerType.JUNIOR, 100000, 100000),
            (EngineerType.SENIOR, 5000, 7500),
            (EngineerType.STAFF, 3000, 6000),
            (EngineerType.TEAM_LEAD, 1000, 3000),
            (EngineerType.ENGINEERING_MANAGER, 1, 4),
        ],
    )
    def test_enums(
        self, engineer_type: EngineerType, salary: int, expected_total_cost: int
    ) -> None:
        engineer = Engineer(name="Ada Lovelace", type=engineer_type, salary=salary)

        total_cost = calculate_engineer_cost(engineer)

        expect(total_cost).to(equal(expected_total_cost))

    def test_raise_an_error_when_creating_with_an_invalid_type(self) -> None:
        invalid_type = "invalid-type"

        error_message = f"Sorry the type '{invalid_type}' is not correct, please use one of {EngineerType.all_values()}"
        try:
            EngineerType.from_(invalid_type)
        except InvalidEngineeringTypeException as ex:
            expect(str(ex)).to(equal(error_message))
