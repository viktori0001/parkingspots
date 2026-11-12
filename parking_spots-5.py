# === Stage 5: Удаление и восстановление ===
# Project: ParkingSpots
class ParkingSpot:
    def __init__(self, number, spot_type, owner):
        self.number = number
        self.spot_type = spot_type
        self.owner = owner
        self.status = "free"
        self.reservation = None
        self.deleted = False

    def soft_delete(self):
        self.deleted = True
        self.status = "removed"
        self.reservation = None

    def restore(self):
        self.deleted = False
        self.status = "free"
        self.reservation = None

    def activate(self, reservation):
        self.status = "reserved"
        self.reservation = reservation

    def occupy(self, vehicle_number):
        self.status = "occupied"
        self.reservation = None

    def free(self):
        self.status = "free"
        self.reservation = None

    def to_dict(self):
        return {
            "number": self.number,
            "spot_type": self.spot_type,
            "owner": self.owner,
            "status": self.status,
            "deleted": self.deleted,
        }

    def __repr__(self):
        state = "soft_deleted" if self.deleted else self.status
        return f"ParkingSpot(number={self.number}, type={self.spot_type}, status={state})"


class ParkingSpotRepository:
    def __init__(self):
        self._spots = {}

    def add(self, spot):
        self._spots[spot.number] = spot

    def get(self, number):
        return self._spots.get(number)

    def all_active(self):
        return [s for s in self._spots.values() if not s.deleted]

    def get_active(self, number):
        spot = self._spots.get(number)
        return spot if spot and not spot.deleted else None

    def soft_delete(self, number):
        spot = self.get_active(number)
        if spot is not None:
            spot.soft_delete()
            return True
        return False

    def restore(self, number):
        spot = self.get_active(number)
        if spot is not None:
            spot.restore()
            return True
        return False

    def remove_permanently(self, number):
        if number in self._spots:
            del self._spots[number]
            return True
        return False

    def __len__(self):
        return len(self._spots)
