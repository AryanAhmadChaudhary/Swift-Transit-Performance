import pandas as pd
import numpy as np

def classify_express(service_type):
    if service_type is None:
        return False

    s = str(service_type).upper()

    express_keywords = ["EXPRESS", "PRIORITY", "OVERNIGHT", "1DAY", "2DAY"]
    return any(kw in s for kw in express_keywords)

def compute_metrics(base_df, events_df):

    metrics = []

    grouped = events_df.sort_values("event_timestamp").groupby("tracking_number")

    for tracking, group in grouped:

        group = group.reset_index(drop=True)

        pickup = group[group["event_type"] == "PU"]["event_timestamp"].min()
        delivery = group[group["event_type"] == "DL"]["event_timestamp"].max()

        if pickup is not None and delivery is not None:
            total_hours = (delivery - pickup).total_seconds() / 3600
        else:
            total_hours = None

        # Facilities
        fac_events = group[group["arrival_location"].str.contains("FACILITY", na=True)]
        num_facilities = fac_events["arrival_location"].nunique()

        # In-transit events
        num_in_transit = sum(group["event_type"] == "IT")
        unique_event_types = group["event_type"].nunique()

        # Delivery attempts
        ood_events = sum(group["event_type"] == "OD")
        first_attempt = (ood_events == 1)

        # time in inter-facility transit
        inter_facility_hours = None
        if len(fac_events) >= 2:
            fac_events = fac_events.sort_values("event_timestamp")
            diffs = fac_events["event_timestamp"].diff().dt.total_seconds() / 3600
            inter_facility_hours = diffs.dropna().sum()

        # avg per facility
        if total_hours and num_facilities > 0:
            avg_hours_per_facility = total_hours / num_facilities
        else:
            avg_hours_per_facility = None

        # is express service
        service_type = base_df.loc[base_df["tracking_number"] == tracking, "service_type"].values[0]
        is_express = classify_express(service_type)

        # delivery location type
        delivery_loc = base_df.loc[base_df["tracking_number"] == tracking, "delivery_location_type"].values
        delivery_loc = delivery_loc[0] if len(delivery_loc) > 0 else None

        row = {
            "tracking_number": tracking,
            "pickup_datetime_ist": pickup,
            "delivery_datetime_ist": delivery,
            "total_transit_hours": total_hours,
            "num_facilities_visited": num_facilities,
            "num_in_transit_events": num_in_transit,
            "time_in_inter_facility_transit_hours": inter_facility_hours,
            "avg_hours_per_facility": avg_hours_per_facility,
            "is_express_service": is_express,
            "delivery_location_type": delivery_loc,
            "num_out_for_delivery_attempts": ood_events,
            "first_attempt_delivery": first_attempt,
            "total_events_count": len(group),
            "unique_event_types_count": unique_event_types,
        }

        metrics.append(row)

    return pd.DataFrame(metrics)
