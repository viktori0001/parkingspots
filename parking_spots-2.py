# === Stage 2: Проверка полей ===
# Project: ParkingSpots
import re


def normalize_plate(plate):
    plate = plate.strip().upper()
    if not re.fullmatch(r"[A-Z]{3}\d{2,3}", plate):
        raise ValueError("Госномер должен содержать 3 буквы и 2-3 цифры")
    return plate


def normalize_type(plate_type):
    plate_type = plate_type.strip().lower()
    if plate_type not in ("стандарт", "vip", "электрокар", "грузовой"):
        raise ValueError("Тип места должен быть одним из: стандарт, vip, электрокар, грузовой")
    return plate_type


def normalize_owner(owner):
    owner = owner.strip()
    if not re.fullmatch(r"[а-яА-ЯёЁ]", owner):
        raise ValueError("Имя владельца должно содержать только кириллические буквы")
    return owner


def normalize_status(status):
    status = status.strip().lower()
    if status not in ("свободно", "занято", "бронь"):
        raise ValueError("Статус должен быть одним из: свободно, занято, бронь")
    return status


def validate_spot(spot_number, plate_type, owner, status):
    spot_number = normalize_plate(spot_number)
    plate_type = normalize_type(plate_type)
    owner = normalize_owner(owner)
    status = normalize_status(status)
    return spot_number, plate_type, owner, status
