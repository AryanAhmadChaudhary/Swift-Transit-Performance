import datetime
from datetime import timezone, timedelta

IST = timezone(timedelta(hours=5, minutes=30))

def get_value(d, path, default=None):
    """
    Safely extract values from deeply nested dictionaries.
    path = ["service", "type"]
    """
    current = d
    for key in path:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

def parse_timestamp(ts):
    """
    Handles timestamps:
    - ISO format
    - MongoDB $numberLong epoch (ms)
    - None or missing values
    Returns datetime in IST.
    """

    if ts is None:
        return None
    if isinstance(ts, dict) and "$numberLong" in ts:
        try:
            epoch_ms = int(ts["$numberLong"])
            return datetime.datetime.fromtimestamp(epoch_ms / 1000, tz=IST)
        except:
            return None
    if isinstance(ts, str):
        try:
            dt = datetime.datetime.fromisoformat(ts)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc).astimezone(IST)
            return dt
        except:
            return None

    return None
