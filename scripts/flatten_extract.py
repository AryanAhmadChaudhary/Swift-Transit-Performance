import pandas as pd
from .utils import get_value, parse_timestamp


def flatten_shipment(shipment):

    td = shipment.get("trackDetails", [])
    if not td:
        return None, None

    td = td[0] 

    tracking = td.get("trackingNumber")
    service_type = get_value(td, ["service", "type"])
    service_description = get_value(td, ["service", "description"])
    carrier = td.get("carrierCode")

    weight = get_value(td, ["packageWeight", "value"])
    weight_units = get_value(td, ["packageWeight", "units"])
    packaging = get_value(td, ["packaging", "type"])

    origin = td.get("shipperAddress", {})
    dest = td.get("destinationAddress", {})

    delivery_location_type = td.get("deliveryLocationType")

    base_row = {
        "tracking_number": tracking,
        "service_type": service_type,
        "service_description": service_description,
        "carrier_code": carrier,
        "package_weight": weight,
        "package_weight_units": weight_units,
        "packaging_type": packaging,
        "origin_city": origin.get("city"),
        "origin_state": origin.get("stateOrProvinceCode"),
        "origin_pincode": origin.get("postalCode"),
        "destination_city": dest.get("city"),
        "destination_state": dest.get("stateOrProvinceCode"),
        "destination_pincode": dest.get("postalCode"),
        "delivery_location_type": delivery_location_type
    }

    events_list = []
    for ev in td.get("events", []):
        ev_dict = {
            "tracking_number": tracking,
            "event_type": ev.get("eventType"),
            "event_description": ev.get("eventDescription"),
            "event_timestamp": parse_timestamp(ev.get("timestamp")),
            "event_city": get_value(ev, ["address", "city"]),
            "event_state": get_value(ev, ["address", "stateOrProvinceCode"]),
            "event_pincode": get_value(ev, ["address", "postalCode"]),
            "arrival_location": ev.get("arrivalLocation")
        }
        events_list.append(ev_dict)

    base_df = pd.DataFrame([base_row])
    events_df = pd.DataFrame(events_list)
    return base_df, events_df


def flatten_all(data):
    base_rows = []
    event_rows = []

    for rec in data:
        base, events = flatten_shipment(rec)
        if base is not None:
            base_rows.append(base)
        if events is not None:
            event_rows.append(events)

    base_df = pd.concat(base_rows, ignore_index=True)
    events_df = pd.concat(event_rows, ignore_index=True)

    return base_df, events_df

if __name__ == "__main__":
    import json
    data = json.load(open("data/shipments.json"))
    b, e = flatten_all(data)
    print(b.head())
    print(e.head())
