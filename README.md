# PyThainance

![PyThainance](https://img.shields.io/badge/Thai-Finance-blue.svg)  
📊 **The Next-Gen Thai Financial Data Library** 🚀

PyThainance is an **open-source financial analysis library** designed to simplify working with **Thai public debt, macroeconomic data, and state enterprise debt**. Built for researchers, policymakers, and developers, PyThainance provides a powerful toolkit for financial data analysis, forecasting, and visualization.

## 🌟 Features

✅ **Data Loader** – Seamlessly import Thailand’s financial datasets from Excel/CSV  
✅ **Debt Analysis** – Compute key indicators like **Debt-to-GDP ratio**, **Government Debt Composition**, and more  
✅ **Visualization** – High-quality financial charts using **Matplotlib & Seaborn**  
✅ **Forecasting Ready** – Compatible with AI/ML models for financial trend prediction  
✅ **Lightweight & Fast** – Optimized for large-scale datasets with Pandas/Numpy  

## 📦 Installation

Install via PyPI (Coming Soon!):
```bash
pip install pythainance
```
Or install from GitHub:
```bash
pip install git+https://github.com/YOUR-ORG/PyThainance.git
```

## 🚀 Quick Start

```python
from pythainance.debt import load_debt_data, compute_government_debt, plot_time_series

# Load Thailand's debt dataset
df = load_debt_data()

# Compute total government debt
gov_debt = compute_government_debt(df)

# Visualize the trend over time
plot_time_series(df.assign(GovernmentDebt=gov_debt), column='GovernmentDebt', title='Thailand Government Debt Trend')
```

## 📊 Example Output

![Debt Trend](https://your-image-url.com/debt_trend.png)

## 📖 Documentation

Comprehensive documentation is coming soon! Stay updated at **[GitHub Wiki](https://github.com/YOUR-ORG/PyThainance/wiki)**.

## 👥 Contributing

We welcome all contributions! If you're interested in contributing, please:
1. Fork this repository
2. Create a new branch
3. Submit a pull request (PR)

For more details, see our **[CONTRIBUTING.md](https://github.com/YOUR-ORG/PyThainance/blob/main/CONTRIBUTING.md)**.

## ⚖️ License

PyThainance is released under the **MIT License**, allowing both personal and commercial use. See the **[LICENSE](https://opensource.org/licenses/MIT)** file for more details.

---

💡 **Follow us for updates!** 🚀

