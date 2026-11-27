# === Stage 12: Быстрые фильтры ===
# Project: ParkingSpots
from datetime import date

def is_today(record, today=None):
    if today is None:
        today = date.today()
    return record.get("start") == today

def is_this_week(record, today=None):
    if today is None:
        today = date.today()
    start = record.get("start")
    end = record.get("end")
    if start is None or end is None:
        return False
    return start <= today <= end

def is_expired(record, today=None):
    if today is None:
        today = date.today()
    return record.get("end") < today

def apply_filter(records, filter_name, today=None):
    if filter_name == "today":
        return [r for r in records if is_today(r, today)]
    if filter_name == "this_week":
        return [r for r in records if is_this_week(r, today)]
    if filter_name == "expired":
        return [r for r in records if is_expired(r, today)]
    return records
