# pythainance/debt/__init__.py

# Re-export functions from the loader, analysis, and visualization modules.
from .loader import setup_debt_data, fix_format_debt_data
from .analysis import (
    load_debt_data,
    compute_government_debt,
    compute_debt_to_gdp_ratio,
    compute_total_debt,
)
from .visualization import plot_time_series, plot_debt_breakdown

__all__ = [
    "setup_debt_data",
    "fix_format_debt_data",
    "load_debt_data",
    "compute_government_debt",
    "compute_debt_to_gdp_ratio",
    "compute_total_debt",
    "plot_time_series",
    "plot_debt_breakdown",
]
