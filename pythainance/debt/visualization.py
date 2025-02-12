# pythainance/debt/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_time_series(df, column, title=None, xlabel="Date", ylabel=None, figsize=(12,6)):
    """
    Plot a time series for a specified column.
    
    Parameters:
        df (DataFrame): DataFrame with a datetime index.
        column (str): The column name to plot.
        title (str, optional): Title of the plot.
        xlabel (str): Label for the x-axis (default: "Date").
        ylabel (str, optional): Label for the y-axis (default: the column name).
        figsize (tuple): Figure size.
    """
    plt.figure(figsize=figsize)
    sns.lineplot(data=df, x=df.index, y=column)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel if ylabel else column)
    if title:
        plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_debt_breakdown(df, columns, title="Debt Breakdown Over Time", figsize=(12,6)):
    """
    Plot a stacked area chart showing the breakdown of debt over time.
    
    Parameters:
        df (DataFrame): DataFrame with a datetime index.
        columns (list): List of column names to include in the breakdown.
        title (str): Title of the plot.
        figsize (tuple): Figure size.
    """
    plt.figure(figsize=figsize)
    df[columns].plot.area()
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
