import os
from importlib import resources
from .loader import setup_debt_data, fix_format_date_debt_data, clean_debt

__all__ = []

# file_path = "dataset/debt.xlsx"
file_path = resources.files("pythainance").joinpath("dataset/debt.xlsx")

# Check if the primary dataset file exists; if not, run the setup and formatting functions
if not os.path.exists(file_path):
    setup_debt_data()
    fix_format_date_debt_data()
    clean_debt()
