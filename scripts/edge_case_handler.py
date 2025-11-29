import pandas as pd

def handle_missing(base_df, events_df):
    """
    Basic cleaning: fill NAs, remove invalid timestamps, fix dtype issues.
    """
    events_df = events_df.dropna(subset=["event_timestamp"])
    base_df = base_df.fillna({"service_type": "UNKNOWN"})
    events_df = events_df.fillna({"event_type": "UNKNOWN"})

    return base_df, events_df
