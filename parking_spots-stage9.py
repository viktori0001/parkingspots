# === Stage 9: Сортировка записей ===
# Project: ParkingSpots
from datetime import datetime


def sort_by_number_descending(spots):
    return sorted(spots, key=lambda spot: spot["number"], reverse=True)


def sort_by_number_ascending(spots):
    return sorted(spots, key=lambda spot: spot["number"])


def sort_by_creation_descending(spots):
    return sorted(
        spots,
        key=lambda spot: spot["created_at"],
        reverse=True,
    )


def sort_by_creation_ascending(spots):
    return sorted(spots, key=lambda spot: spot["created_at"])


if __name__ == "__main__":
    sample_spots = [
        {
            "number": 12,
            "type": "electric",
            "owner": "Иванов",
            "status": "free",
            "created_at": datetime(2024, 1, 15),
        },
        {
            "number": 7,
            "type": "standard",
            "owner": "Петров",
            "status": "reserved",
            "created_at": datetime(2024, 2, 3),
        },
        {
            "number": 3,
            "type": "standard",
            "owner": "Сидоров",
            "status": "occupied",
            "created_at": datetime(2024, 1, 20),
        },
    ]

    print("По номеру (убывание):")
    for spot in sort_by_number_descending(sample_spots):
        print(spot["number"])

    print("По номеру (возрастание):")
    for spot in sort_by_number_ascending(sample_spots):
        print(spot["number"])

    print("По дате создания (убывание):")
    for spot in sort_by_creation_descending(sample_spots):
        print(spot["created_at"])

    print("По дате создания (возрастание):")
    for spot in sort_by_creation_ascending(sample_spots):
        print(spot["created_at"])
