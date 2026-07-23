
import json
from datetime import date, datetime, timedelta
import re

PLACEHOLDER_DATE = "YYYY-MM-DD"
PLACEHOLDER_TIME = "HH:MM:SS"

LIST_FIELDS = ["attendees", "topics_discussed", "materials_shared",
               "samples_distributed", "follow_up_actions"]

def normalize_list_field(value):
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        stripped = value.strip()
        # handles "[]", "['a','b']", etc.
        try:
            parsed = json.loads(stripped)
            if isinstance(parsed, list):
                return parsed
        except json.JSONDecodeError:
            pass
        if stripped == "":
            return []
        return [stripped]  # single value string -> wrap it
    return []



FUZZY_DATE_MAP = {
    "today": 0,
    "yesterday": -1,
    "day before yesterday": -2,
    "the day before yesterday": -2,
    "tomorrow": 1,
    "day after tomorrow": 2,
    "the day after tomorrow": 2,
}

WEEKDAYS = {
    "monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3,
    "friday": 4, "saturday": 5, "sunday": 6,
}

def normalize_date(value: str | None, reference: datetime | None = None) -> str | None:
    """
    Resolve an LLM-extracted date string to YYYY-MM-DD.
    `reference` = the actual timestamp of the conversation/interaction
    (defaults to now if not provided).
    """
    ref_date = (reference or datetime.now()).date()

    if not value:
        return None

    v = value.strip().lower()

    if v == "yyyy-mm-dd":  # placeholder guard from earlier
        return None

    # 1. Direct fuzzy matches
    if v in FUZZY_DATE_MAP:
        return (ref_date + timedelta(days=FUZZY_DATE_MAP[v])).isoformat()

    # 2. "N days ago" / "N days back"
    m = re.match(r"(\d+)\s+days?\s+ago", v)
    if m:
        return (ref_date - timedelta(days=int(m.group(1)))).isoformat()

    # 3. "last <weekday>" / "this <weekday>"
    m = re.match(r"(last|this)\s+(\w+)", v)
    if m and m.group(2) in WEEKDAYS:
        target_wd = WEEKDAYS[m.group(2)]
        delta = (ref_date.weekday() - target_wd) % 7
        delta = delta if delta != 0 else 7  # "last monday" shouldn't be today
        return (ref_date - timedelta(days=delta)).isoformat()

    # 4. "last week" -> approximate to 7 days ago (adjust as needed)
    if v == "last week":
        return (ref_date - timedelta(days=7)).isoformat()

    # 5. Already a real date string
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return value
    except ValueError:
        pass

    # 6. Unparseable -> None, let the fallback (below) handle it
    return None

FUZZY_TIME_MAP = {
    "morning": "09:00:00",
    "afternoon": "14:00:00",
    "evening": "18:00:00",
    "night": "20:00:00",
}

def normalize_time(value):
    if not value:
        return None
    v = value.strip().lower()
    if v == PLACEHOLDER_TIME.lower():
        return None
    if v in FUZZY_TIME_MAP:
        return FUZZY_TIME_MAP[v]
    try:
        datetime.strptime(value, "%H:%M:%S")
        return value
    except ValueError:
        return None  # unparseable -> None, don't crash
