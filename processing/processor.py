import pandas as pd

def normalize_data(df):
    
    # Title case names
    df["First Name"] = df["First Name"].str.title()
    df["Last Name"] = df["Last Name"].str.title()

    # Clean phone numbers (remove non-digit characters)
    df["Phone Number"] = df["Phone Number"].str.replace(r"\D", "", regex=True)

    # Add Full Name
    df["Full Name"] = df["First Name"] + " " + df["Last Name"]

    return df
