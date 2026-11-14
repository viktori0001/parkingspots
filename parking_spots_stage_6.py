# === Stage 6: Связанная сущность ===
# Project: ParkingSpots
from datetime import datetime, timedelta


class Booking:
    def __init__(self, spot_id, user_id, start_time, end_time):
        self.id = datetime.now().strftime("%Y%m%d%H%M%S")
        self.spot_id = spot_id
        self.user_id = user_id
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return (
            f"Booking(id={self.id}, spot_id={self.spot_id}, "
            f"user_id={self.user_id}, start_time={self.start_time}, "
            f"end_time={self.end_time})"
        )


def add_booking(bookings, spot_id, user_id, start_time, end_time):
    booking = Booking(spot_id, user_id, start_time, end_time)
    bookings.append(booking)
    return booking
