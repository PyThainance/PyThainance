# pythainance/debt/loader.py

import os
import pandas as pd
from datetime import datetime

def setup_debt_data():
    """
    Load data from the backup dataset and transform it to the desired format.
    """
    df = pd.read_excel("pythainance/dataset/backup_dataset/debt.xlsx", skiprows=[0])
    # Transpose the DataFrame so that dates become the index
    df = df.T
    df.columns = df.iloc[0]
    df = df[1:]
    # Save the transformed data to the primary dataset file
    df.to_excel("pythainance/dataset/debt.xlsx", index=True)

def fix_format_debt_data():
    """
    Convert Thai date formats to datetime objects and sort the data by date.
    """
    df = pd.read_excel("pythainance/dataset/debt.xlsx")
    
    thai_months = {
        "ม.ค.": 1, "ก.พ.": 2, "มี.ค.": 3, "เม.ย.": 4, "พ.ค.": 5, "มิ.ย.": 6,
        "ก.ค.": 7, "ส.ค.": 8, "ก.ย.": 9, "ต.ค.": 10, "พ.ย.": 11, "ธ.ค.": 12
    }

    def convert_thai_date(thai_date):
        # Assumes input format is "ม.ค. 2548"
        month_thai, year_thai = thai_date.split(" ")
        month = thai_months[month_thai]
        year = int(year_thai) - 543  # Convert from Thai Buddhist year to Gregorian year
        return datetime(year, month, 1)

    # Assume that the first column contains Thai date strings
    df["date"] = df.iloc[:, 0].astype(str).apply(convert_thai_date)
    df.set_index("date", inplace=True)
    df.sort_index(inplace=True)
    # Format the index as 'dd/mm/YYYY'
    df.index = df.index.strftime('%d/%m/%Y')
    # Drop the original first column if it's no longer needed
    df = df.drop(df.columns[0], axis=1)
    df.to_excel("pythainance/dataset/debt.xlsx", index=True)

# Check if the primary dataset file exists; if not, run the setup and formatting functions
file_path = "pythainance/dataset/debt.xlsx"
if not os.path.exists(file_path):
    setup_debt_data()
    fix_format_debt_data()
