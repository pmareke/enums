from src.engineer import Engineer, EngineerType


def calculate_engineer_cost(engineer: Engineer) -> float:
    return engineer.salary * hour_rate(engineer.type)


def hour_rate(engineer_type: EngineerType) -> float:
    return {
        EngineerType.JUNIOR: 1,
        EngineerType.SENIOR: 1.5,
        EngineerType.STAFF: 2,
        EngineerType.TEAM_LEAD: 3,
        EngineerType.ENGINEERING_MANAGER: 4,
    }[engineer_type]
