import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from ingestion import scraper

class TestScraper(unittest.TestCase):

    @patch('ingestion.scraper.download_file')
    def test_csv_file_download(self, mock_download):
        mock_download.return_value = "test_download.csv"
        scraper.download_file("https://fakeurl.com/test.csv", "test_download.csv")
        mock_download.assert_called_once()

    @patch('pandas.read_csv')
    def test_csv_file_extraction(self, mock_read_csv):
        mock_df = MagicMock()
        mock_read_csv.return_value = mock_df
        df = scraper.parse_file("test_download.csv", "text/csv")
        self.assertEqual(df, mock_df)
        mock_read_csv.assert_called_once_with("test_download.csv")

    def test_file_type_detection(self):
        self.assertEqual(scraper.detect_file_type("data.csv"), "text/csv")
        self.assertEqual(scraper.detect_file_type("data.xlsx"), "excel")
        self.assertEqual(scraper.detect_file_type("data.unknown"), "unknown")

    def test_data_structure_validation(self):
        df = pd.DataFrame({
            "Employee ID": [1],
            "First Name": ["John"],
            "Last Name": ["Doe"],
            "Email": ["john@example.com"],
            "Job Title": ["Engineer"],
            "Phone Number": ["1234567890"],
            "Hire Date": ["2022-01-01"]
        })
        self.assertTrue(scraper.is_valid_structure(df))

    def test_invalid_data_structure(self):
        df = pd.DataFrame({"Name": ["Missing required columns"]})
        self.assertFalse(scraper.is_valid_structure(df))

if __name__ == "__main__":
    unittest.main()
