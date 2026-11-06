# === Stage 3: Хранилище в памяти ===
# Project: ParkingSpots
import uuid
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ParkingSpot:
    number: str
    spot_type: str = "guest"
    owner: Optional[str] = None
    status: str = "free"
    id: str = field(default_factory=lambda: uuid.uuid4().hex)


class ParkingSpotsStore:
    def __init__(self) -> None:
        self._spots: dict[str, ParkingSpot] = {}

    def add(self, spot: ParkingSpot) -> ParkingSpot:
        self._spots[spot.id] = spot
        return spot

    def add_from_number(
        self,
        number: str,
        spot_type: str = "guest",
        owner: Optional[str] = None,
    ) -> ParkingSpot:
        spot = ParkingSpot(number=number, spot_type=spot_type, owner=owner)
        return self.add(spot)

    def get(self, spot_id: str) -> Optional[ParkingSpot]:
        return self._spots.get(spot_id)

    def get_by_number(self, number: str) -> Optional[ParkingSpot]:
        for spot in self._spots.values():
            if spot.number == number:
                return spot
        return None

    def list_all(self) -> List[ParkingSpot]:
        return list(self._spots.values())

    def list_by_type(self, spot_type: str) -> List[ParkingSpot]:
        return [spot for spot in self._spots.values() if spot.spot_type == spot_type]

    def list_free(self) -> List[ParkingSpot]:
        return [spot for spot in self._spots.values() if spot.status == "free"]

    def update(self, spot_id: str, **changes: object) -> bool:
        spot = self._spots.get(spot_id)
        if spot is None:
            return False
        for key, value in changes.items():
            setattr(spot, key, value)
        return True
