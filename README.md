# Employee Data Scraper & Processor

This project helps in downloading, validating, and processing employee data from a file stored on the Google Drive. The goal is to clean and structure the data so it can be used for further analysis or even be stored in a data warehouse.

---

## User Story

**Title:** Scraping Employee Data from Google Drive File

As a developer,
I want to scrape employee data from the provided Google Drive file URL ([https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK\_RHiNsE8fjPCVK\&export=download](https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download)),
so that I can ingest the data into our data warehouse for further analysis.

---

## Acceptance Criteria

### File Download:

* The scraper should download the file from the given Google Drive link.
* The downloaded file should be valid (CSV or Excel).

### Data Structure Validation:

* The file type should be identified (CSV, Excel, etc.).
* The file should be read into a proper DataFrame.
* The columns should include:

  * Employee ID
  * First Name
  * Last Name
  * Email
  * Job Title
  * Phone Number
  * Hire Date

### Error Handling:

* If the file can’t be downloaded, it should retry a few times and log the error.
* If the file format is invalid, an error message should be shown and logged.

---

## Test Cases

1. Verify that the CSV file is downloaded successfully.
2. Verify that the CSV file is read into a DataFrame.
3. Validate that the file type is correctly detected.
4. Check if the DataFrame contains all required columns.
5. Ensure missing or invalid data is detected and handled.

---

## Folder Structure

```
employee_scraper_project/
│
├── ingestion/
│   ├── main.py              # Starts ingestion phase
│   ├── scraper.py           # Download, parse, and validate data
│   ├── run_scraper.json     # Config with scraper ID and URL
│   └── test_scraper.py      # Tests for scraper
│
├── processing/
│   ├── main.py              # Starts processing phase
│   ├── processor.py         # Data normalization logic
│   └── test_processor.py    # Tests for data processor
│
├── utils/                   # Placeholder for utilities
│
├── employee_data.csv                 # Downloaded raw file
├── validated_employee_data.csv       # After validation
├── processed_employee_data.csv       # Final cleaned file
├── pipeline.py                       # Runs ingestion + processing
├── requirements.txt                  # All Python dependencies
└── README.md                         # Project documentation
```

---

## How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run full pipeline

```
python pipeline.py
```

### 3. Or run in steps

* Run ingestion:

  ```
  python ingestion/main.py
  ```

* Run processing:

  ```
  python processing/main.py
  ```

---

## How to Run Tests

```
python -m unittest ingestion.test_scraper
python -m unittest processing.test_processor
```

