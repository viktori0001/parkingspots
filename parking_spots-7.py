# === Stage 7: Связи между сущностями ===
# Project: ParkingSpots
from datetime import datetime, date


class ParkingSpot:
    """Парковочное место двора."""

    def __init__(self, number, spot_type, owner, status="free"):
        self.number = number
        self.spot_type = spot_type
        self.owner = owner
        self.status = status

    def __repr__(self):
        return (f"ParkingSpot(number={self.number}, "
                f"spot_type={self.spot_type}, "
                f"owner={self.owner}, status={self.status})")


class Reservation:
    """Бронирование парковочного места."""

    def __init__(self, spot_number, start_date, end_date, owner=None):
        self.spot_number = spot_number
        self.start_date = start_date
        self.end_date = end_date
        self.owner = owner

    def __repr__(self):
        return (f"Reservation(spot_number={self.spot_number}, "
                f"start_date={self.start_date}, "
                f"end_date={self.end_date}, owner={self.owner})")


def get_reservations_for_spot(spot, reservations):
    """Получить все брони для заданного места по номеру."""
    target_number = spot.number
    return [reservation for reservation in reservations
            if reservation.spot_number == target_number]


def validate_reservation_integrity(spot, reservation):
    """Проверить целостность связи между местом и бронью.

    Возвращает True, если бронь относится к нужному месту,
    имеет корректный диапазон дат и не перекрывает владельца.
    """
    if spot.number != reservation.spot_number:
        return False

    if reservation.start_date > reservation.end_date:
        return False

    today = date.today()
    if reservation.start_date < today:
        return False

    if reservation.owner is not None and reservation.owner != spot.owner:
        return False

    return True


def get_valid_reservations_for_spot(spot, reservations):
    """Получить валидные брони для места с проверкой целостности."""
    target_number = spot.number
    valid = []
    for reservation in reservations:
        if reservation.spot_number == target_number and \
                validate_reservation_integrity(spot, reservation):
            valid.append(reservation)
    return valid


if __name__ == "__main__":
    spot = ParkingSpot(5, "premium", "ivanov")
    reservations = [
        Reservation(5, date(2025, 1, 1), date(2025, 1, 10), "ivanov"),
        Reservation(5, date(2025, 1, 20), date(2025, 1, 25), "petrov"),
        Reservation(6, date(2025, 1, 1), date(2025, 1, 5), "ivanov"),
    ]

    print(get_reservations_for_spot(spot, reservations))
    print(get_valid_reservations_for_spot(spot, reservations))
