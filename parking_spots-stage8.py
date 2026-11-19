# === Stage 8: Генерация идентификаторов ===
# Project: ParkingSpots
import uuid
import string
import datetime


PROJECT_PREFIX = "PS"


def generate_unique_id(prefix: str, length: int = 6) -> str:
    """Генерация уникального идентификатора с префиксом проекта."""
    alphabet = string.ascii_lowercase + string.digits
    while True:
        unique_part = "".join(alphabet[int(random.choice(range(len(alphabet))))] for _ in range(length))
        candidate = f"{prefix}-{unique_part}"
        if candidate not in _used_ids:
            _used_ids.add(candidate)
            return candidate


def is_available(id_value: str, reserved: set) -> bool:
    """Проверка отсутствия коллизии с уже зарезервированными идентификаторами."""
    return id_value not in reserved


def reserve_id(prefix: str, reserved: set) -> str:
    """Забронировать уникальный идентификатор, поместив его в резерв."""
    id_value = generate_unique_id(prefix, reserved=reserved)
    reserved.add(id_value)
    return id_value


_used_ids = set()


def new_spot_id() -> str:
    return generate_unique_id(PROJECT_PREFIX)


def new_booking_id() -> str:
    return generate_unique_id(PROJECT_PREFIX, length=8)


if __name__ == "__main__":
    ids = {new_spot_id() for _ in range(5)}
    print(ids)
    assert len(ids) == 5, "Уникальность нарушена!"
    print("Все идентификаторы уникальны")
