import os
import numpy as np
import pandas as pd
from datetime import datetime

def setup_debt_data():
    """
    Load data from the backup dataset and transform it to the desired format.
    """
    df = pd.read_excel("dataset/backup_dataset/debt.xlsx", skiprows=[0])
    df = df.T
    df.columns = df.iloc[0]
    df = df[1:]
    df.to_excel("dataset/debt.xlsx", index=True)

def fix_format_date_debt_data():
    """
    Convert Thai date formats to datetime objects, add 'month' and 'year' columns,
    and sort the data by date.
    """
    df = pd.read_excel("dataset/debt.xlsx")

    thai_months = {
        "ม.ค.": 1, "ก.พ.": 2, "มี.ค.": 3, "เม.ย.": 4, "พ.ค.": 5, "มิ.ย.": 6,
        "ก.ค.": 7, "ส.ค.": 8, "ก.ย.": 9, "ต.ค.": 10, "พ.ย.": 11, "ธ.ค.": 12
    }

    def convert_thai_date(thai_date):
        month_thai, year_thai = thai_date.split(" ")
        month = thai_months[month_thai]
        year = int(year_thai) - 543
        return datetime(year, month, 1)

    df["date"] = df.iloc[:, 0].astype(str).apply(convert_thai_date)
    df["month"] = df["date"].dt.month
    df["year"] = df["date"].dt.year

    column_order = ["date", "month", "year"] + [col for col in df.columns if col not in ["date", "month", "year"]]
    df = df[column_order]

    df.set_index("date", inplace=True)
    df.sort_index(inplace=True)
    df.index = df.index.strftime('%d/%m/%Y')

    df.to_excel("dataset/debt.xlsx", index=True)
    
def clean_debt():
    """
    clean and return the debt data.
    """
    df = pd.read_excel("dataset/debt.xlsx", thousands=",")
    df = df.iloc[:, :-2]
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
    df.to_excel("dataset/debt.xlsx", index=False)

def get_debt_data():
    """
    Load and return the debt data.
    """
    df = pd.read_excel("dataset/debt.xlsx")
    return df
