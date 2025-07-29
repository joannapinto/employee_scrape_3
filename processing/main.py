import pandas as pd
import os
from processor import normalize_data

REQUIRED_COLUMNS = [
    "Employee ID", "First Name", "Last Name",
    "Email", "Job Title", "Phone Number", "Hire Date"
]

def main():
    input_file = "validated_employee_data.csv"
    output_file = "processed_employee_data.csv"

    if not os.path.exists(input_file):
        print(" Validated data not found. Run the ingestion phase first.")
        return

    df = pd.read_csv(input_file)


    # Validate column structure
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        print(f" Missing required columns: {missing_cols}")
        print(" Skipping processing due to invalid structure.")
        return

    #  Clean and normalize
    df = normalize_data(df)
    df.to_csv(output_file, index=False)

    print(" Data normalization complete. Output saved as:", output_file)
    

if __name__ == "__main__":
    main()
