import json
import pandas as pd

def load_json(path="data/shipments.json"):
    with open(path, "r") as f:
        data = json.load(f)
    return data

def explore_data(data):
    print("Total records:", len(data))
    print("\nTop-level keys in first record:", list(data[0].keys()))

    sample = data[0]
    if "trackDetails" in sample and len(sample["trackDetails"]) > 0:
        print("\nFields inside trackDetails[0]:", list(sample["trackDetails"][0].keys()))
        print("\nEvent count:", len(sample["trackDetails"][0].get("events", [])))

if __name__ == "__main__":
    data = load_json()
    explore_data(data)
