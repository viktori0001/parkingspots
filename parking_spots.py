# === Stage 1: Каркас модуля ===
# Project: ParkingSpots
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List


class ParkingSpotStatus(str, Enum):
    FREE = "free"
    RESERVED = "reserved"
    OCCUPIED = "occupied"


@dataclass
class ParkingSpot:
    number: str
    spot_type: str = "regular"
    owner: str = ""
    status: ParkingSpotStatus = ParkingSpotStatus.FREE

    def __post_init__(self) -> None:
        self.status = ParkingSpotStatus(self.status)


def create_demo_spots() -> List[ParkingSpot]:
    return [
        ParkingSpot("A1", "regular", "Иванов И.И.", ParkingSpotStatus.FREE),
        ParkingSpot("B2", "handicap", "МФУ «Городской»", ParkingSpotStatus.FREE),
        ParkingSpot("C3", "regular", "", ParkingSpotStatus.FREE),
        ParkingSpot("D4", "regular", "Петрова А.С.", ParkingSpotStatus.RESERVED),
        ParkingSpot("E5", "electric", "ЗАО «Энерго»", ParkingSpotStatus.OCCUPIED),
        ParkingSpot("F6", "regular", "", ParkingSpotStatus.FREE),
    ]


def print_spots(spots: List[ParkingSpot]) -> None:
    print("Парковочные места двора")
    print("-" * 30)
    for spot in spots:
        print(f"{spot.number} [{spot.spot_type:8}] "
              f"владелец: {spot.owner or '-':15} "
              f"статус: {spot.status.value}")
    print("-" * 30)
    print(f"Всего: {len(spots)} | "
          f"свободно: {sum(1 for s in spots if s.status is ParkingSpotStatus.FREE)}")


def main() -> None:
    spots = create_demo_spots()
    print_spots(spots)
    print(f"Сформирован каркас ParkingSpots. "
          f"Готов к Этапу 2: бронирование.")


if __name__ == "__main__":
    main()
