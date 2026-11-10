# === Stage 4: Редактирование записей ===
# Project: ParkingSpots
from typing import Optional, Dict, Any


ALLOWED_FIELDS = ("номер", "тип", "владелец")


class ParkingSpot:
    def __init__(self, номер: str, тип: str, владелец: str, статус: str):
        self.номер = номер
        self.тип = тип
        self.владелец = владелец
        self.статус = статус

    def to_dict(self) -> Dict[str, Any]:
        return {
            "номер": self.номер,
            "тип": self.тип,
            "владелец": self.владелец,
            "статус": self.статус,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ParkingSpot":
        return cls(
            номер=data["номер"],
            тип=data["тип"],
            владелец=data["владелец"],
            статус=data["статус"],
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ParkingSpot):
            return NotImplemented
        return self.to_dict() == other.to_dict()

    def __repr__(self) -> str:
        return f"ParkingSpot({self.to_dict()})"


def update_spot_by_id(
    spots: Dict[str, ParkingSpot],
    identifier: str,
    changes: Dict[str, Any],
) -> Optional[ParkingSpot]:
    if identifier not in spots:
        return None

    current = spots[identifier]
    new_values = {key: current.__dict__[key] for key in current.__dict__}
    for key, value in changes.items():
        if key not in ALLOWED_FIELDS:
            raise ValueError(f"Поле '{key}' нельзя изменить")
        if key not in new_values:
            raise ValueError(f"Поле '{key}' не существует")
        new_values[key] = value

    updated = ParkingSpot(
        номер=new_values["номер"],
        тип=new_values["тип"],
        владелец=new_values["владелец"],
        статус=new_values["статус"],
    )
    spots[identifier] = updated
    return updated
