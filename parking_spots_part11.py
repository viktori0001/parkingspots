# === Stage 11: Теги ===
# Project: ParkingSpots
from datetime import datetime


def add_tag(parking_spot, tag):
    if parking_spot.tags is None:
        parking_spot.tags = set()
    parking_spot.tags.add(tag)


def remove_tag(parking_spot, tag):
    if parking_spot.tags:
        parking_spot.tags.discard(tag)


def search_by_tag(parking_spots, tag):
    return [spot for spot in parking_spots if tag in (spot.tags or set())]


class ParkingSpot:
    def __init__(self, number, type, owner, status):
        self.number = number
        self.type = type
        self.owner = owner
        self.status = status
        self.tags = None

    def __repr__(self):
        return f"ParkingSpot(number={self.number}, type={self.type}, owner={self.owner}, status={self.status}, tags={self.tags})"
