# === Stage 10: Текстовый поиск ===
# Project: ParkingSpots
import re


def highlight_matches(text, needles):
    """Подсвечивает вхождения needle в строку text."""
    if not text:
        return ""
    result = text
    for needle in needles:
        if not needle:
            continue
        pattern = re.escape(needle)
        result = re.sub(
            pattern,
            lambda m: "\033[1m" + m.group(0) + "\033[0m",
            result,
            flags=re.IGNORECASE,
        )
    return result


class ParkingSpot:
    def __init__(self, number, spot_type, owner, status):
        self.number = number
        self.spot_type = spot_type
        self.owner = owner
        self.status = status

    def __repr__(self):
        return (
            f"ParkingSpot(number={self.number!r}, "
            f"spot_type={self.spot_type!r}, "
            f"owner={self.owner!r}, status={self.status!r})"
        )


def find_spots_by_text(spots, needles):
    """Находит места по текстовым полям с учётом регистра."""
    matches = []
    for spot in spots:
        searchable = [spot.number, spot.spot_type, spot.owner, spot.status]
        if any(needle in field for field in searchable for needle in needles):
            matches.append(spot)
    return matches


if __name__ == "__main__":
    sample_spots = [
        ParkingSpot("A1", "VIP", "Иванов", "free"),
        ParkingSpot("B2", "standard", "Петров", "reserved"),
        ParkingSpot("C3", "disabled", "Сидоров", "occupied"),
        ParkingSpot("D4", "vip", "Кузнецов", "free"),
    ]

    needles = ["ив"]
    matches = find_spots_by_text(sample_spots, needles)
    for spot in matches:
        print(highlight_matches(repr(spot), needles))
