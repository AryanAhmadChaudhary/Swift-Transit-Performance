import pandas as pd

def generate_detailed(base_df, metrics_df, out_path="output/transit_performance_detailed.csv"):
    final = base_df.merge(metrics_df, on="tracking_number", how="left")
    final.to_csv(out_path, index=False)

def generate_summary(metrics_df, base_df, out_path="output/transit_performance_summary.csv"):

    summary = {}

    # Overall metrics
    summary["total_shipments_analyzed"] = len(metrics_df)
    summary["avg_transit_hours"] = metrics_df["total_transit_hours"].mean()
    summary["median_transit_hours"] = metrics_df["total_transit_hours"].median()
    summary["std_dev_transit_hours"] = metrics_df["total_transit_hours"].std()
    summary["min_transit_hours"] = metrics_df["total_transit_hours"].min()
    summary["max_transit_hours"] = metrics_df["total_transit_hours"].max()

    # Facility metrics
    summary["avg_facilities_per_shipment"] = metrics_df["num_facilities_visited"].mean()
    summary["median_facilities_per_shipment"] = metrics_df["num_facilities_visited"].median()
    summary["mode_facilities_per_shipment"] = metrics_df["num_facilities_visited"].mode().iloc[0]

    summary["avg_hours_per_facility"] = metrics_df["avg_hours_per_facility"].mean()
    summary["median_hours_per_facility"] = metrics_df["avg_hours_per_facility"].median()

    # Delivery performance
    summary["pct_first_attempt_delivery"] = metrics_df["first_attempt_delivery"].mean()
    summary["avg_out_for_delivery_attempts"] = metrics_df["num_out_for_delivery_attempts"].mean()

    # Service type comparison
    service_groups = base_df.merge(metrics_df, on="tracking_number").groupby("service_type")

    service_summary = service_groups["total_transit_hours"].mean().rename("avg_transit_hours_by_service_type")
    facilities_summary = service_groups["num_facilities_visited"].mean().rename("avg_facilities_by_service_type")
    service_counts = service_groups.size().rename("count_shipments_by_service_type")

    combined_service = pd.concat([service_summary, facilities_summary, service_counts], axis=1)

    summary_df = pd.DataFrame([summary])
    summary_df.to_csv(out_path, index=False)

    combined_service.to_csv("output/service_type_analysis.csv")

