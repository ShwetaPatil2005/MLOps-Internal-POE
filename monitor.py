import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

# Small synthetic datasets keep this monitoring dry run reproducible.
reference_data = pd.DataFrame({
    "quantity": [5, 7, 8, 10, 12, 9, 6, 11, 7, 10, 8, 9, 6, 12, 10, 7, 8, 11, 9, 10],
    "unit_price": [2.5, 3.0, 3.5, 4.0, 2.8, 3.2, 4.1, 3.7, 2.9, 3.6, 3.1, 4.2, 3.3, 2.7, 3.8, 3.4, 4.0, 3.0, 3.6, 3.2],
})
# Current data is intentionally shifted to demonstrate data-drift reporting.
current_data = pd.DataFrame({
    "quantity": [8, 11, 12, 15, 18, 14, 9, 16, 11, 15, 12, 14, 9, 18, 15, 11, 12, 16, 14, 15],
    "unit_price": [3.0, 3.6, 4.2, 4.8, 3.4, 3.8, 4.9, 4.4, 3.5, 4.3, 3.7, 5.0, 4.0, 3.2, 4.6, 4.1, 4.8, 3.6, 4.3, 3.8],
})

def main():
    report = Report(metrics=[DataDriftPreset()])
    result = report.run(reference_data=reference_data, current_data=current_data)
    result.save_html("evidently_report.html")
    print("Evidently monitoring run completed.")
    print("Reference rows:", len(reference_data))
    print("Current rows:", len(current_data))
    print("HTML report saved to evidently_report.html")
    print("Note: current data is intentionally shifted for demonstration.")

if __name__ == "__main__":
    main()
