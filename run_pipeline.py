import json
from scripts.load_and_explore import load_json
from scripts.flatten_extract import flatten_all
from scripts.edge_case_handler import handle_missing
from scripts.compute_metrics import compute_metrics
from scripts.generate_output_csvs import generate_detailed, generate_summary

def run_pipeline():

    print("Loading JSON…")
    data = load_json()

    print("Flattening shipments…")
    base_df, events_df = flatten_all(data)

    print("Cleaning & handling edge cases…")
    base_df, events_df = handle_missing(base_df, events_df)

    print("Computing metrics…")
    metrics_df = compute_metrics(base_df, events_df)

    print("Generating CSV outputs…")
    generate_detailed(base_df, metrics_df)
    generate_summary(metrics_df, base_df)

    print("Pipeline completed successfully!")
    print("Outputs saved in /output/")

if __name__ == "__main__":
    run_pipeline()
