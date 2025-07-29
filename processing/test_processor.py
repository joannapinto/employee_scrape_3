import unittest
import pandas as pd
from processing.processor import normalize_data  

class TestNormalizeEmployeeData(unittest.TestCase):

    def test_normalize_data_logic(self):
        df = pd.DataFrame({
            "Employee ID": ["001"],
            "First Name": ["JOHN"],
            "Last Name": ["DOE"],
            "Email": ["JOHN.DOE@EXAMPLE.COM"],
            "Job Title": ["Engineer"],
            "Phone Number": ["+1-800-123-4567"],
            "Hire Date": ["2022-01-15"]
        })

        processed_df = normalize_data(df)

        self.assertEqual(processed_df["First Name"].iloc[0], "John")
        self.assertEqual(processed_df["Phone Number"].iloc[0], "18001234567")
        self.assertEqual(processed_df["Full Name"].iloc[0], "John Doe")

if __name__ == "__main__":
    unittest.main()
