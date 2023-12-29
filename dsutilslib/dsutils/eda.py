import chardet

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from ipywidgets import interact, Dropdown
from typing import List


### Functions with tests ###
def detect_encoding(filepath: str) -> str:
    with open(filepath, "rb") as f:
        result = chardet.detect(f.read())
    encoding = result["encoding"]
    return encoding


def describe_all(df: pd.DataFrame):
    """
    Get a summary of datatypes from a dataframe.
    """
    return df.describe(include="all")


### Functions without tests ###
def create_histogram_plot(
    df: pd.DataFrame, categorical_vars: list, numerical_var: str, bins: int
):
    """
    Creates an interactive histogram for a given numerical variable, with filters based on categorical variables.

    Args:
        df (pd.DataFrame): The dataframe with the data.
        categorical_vars (list): List of categorical variable names to filter data.
        numerical_var (str): Name of the numerical variable for histogram.
        bins (int): Number of bins for the histogram.
    """

    def _interactive_histogram_plot(**kwargs):
        filtered_df = df.copy()
        for cat_var, selected_val in kwargs.items():
            filtered_df = filtered_df[filtered_df[cat_var] == selected_val]

        x = filtered_df[numerical_var].dropna()

        if len(x) > 0:
            plt.figure(figsize=(12, 6))
            sns.histplot(x, bins=bins, kde=False)
            plt.xlabel(f"{numerical_var} Values", fontsize=12)
            plt.ylabel("Frequency", fontsize=12)
            plt.title(f"Histogram of {numerical_var}", fontsize=15)
            plt.show()
        else:
            print("No data available for the selected criteria.")

    # Creating dynamic widgets for each categorical variable
    widgets_dict = {
        var: Dropdown(options=df[var].unique(), description=var)
        for var in categorical_vars
    }

    # Creating the interactive plot
    interact(_interactive_histogram_plot, **widgets_dict)


def create_boxplot(
    df: pd.DataFrame,
    filter_categories: List[str],
    plot_category: str,
    numerical_var: str,
):
    """
    Creates an interactive boxplot for a given numerical variable, grouped by a categorical variable, with filters based on other categorical variables.

    Args:
        df (pd.DataFrame): The dataframe with the data.
        filter_categories (List(str)): List of categorical variable names to filter data.
        plot_category (str): Categorical variable name for grouping data in the boxplot.
        numerical_var (str): Numerical variable for the boxplot.

    Example usage
        create_boxplot(your_dataframe, ['Category1', 'Category2'], 'GroupCategory', 'NumericalColumn')
    """

    def _interactive_boxplot(**kwargs):
        filtered_df = df.copy()
        for cat_var, selected_val in kwargs.items():
            filtered_df = filtered_df[filtered_df[cat_var] == selected_val]

        plt.figure(figsize=(17, 7))
        sns.boxplot(data=filtered_df, x=plot_category, y=numerical_var)
        plt.title(f"Boxplot of {numerical_var} by {plot_category}", fontsize=15)
        plt.xlabel(f"{plot_category}", fontsize=12)
        plt.ylabel(f"{numerical_var}", fontsize=12)
        plt.xticks(rotation=45)
        plt.show()

    # Creating dynamic widgets for filtering
    filter_widgets_dict = {
        var: Dropdown(options=df[var].unique(), description=var)
        for var in filter_categories
    }

    # Creating the interactive plot
    interact(_interactive_boxplot, **filter_widgets_dict)


# Could alternatively make the plot function above generalize to take either boxplot or violinplot.
def create_violinplot(
    df: pd.DataFrame,
    filter_categories: List[str],
    plot_category: str,
    numerical_var: str,
):
    """
    Creates an interactive violinplot for a given numerical variable, grouped by a categorical variable, with filters based on other categorical variables.

    Args:
        df (pd.DataFrame): The dataframe with the data.
        filter_categories (List(str)): List of categorical variable names to filter data.
        plot_category (str): Categorical variable name for grouping data in the violinplot.
        numerical_var (str): Numerical variable for the violinplot.

    Example usage
        create_violinplot(your_dataframe, ['Category1', 'Category2'], 'GroupCategory', 'NumericalColumn')
    """

    def _interactive_violinplot(**kwargs):
        filtered_df = df.copy()
        for cat_var, selected_val in kwargs.items():
            filtered_df = filtered_df[filtered_df[cat_var] == selected_val]

        plt.figure(figsize=(17, 7))
        sns.violinplot(data=filtered_df, x=plot_category, y=numerical_var, cut=0)
        plt.title(f"Violinplot of {numerical_var} by {plot_category}", fontsize=15)
        plt.xlabel(f"{plot_category}", fontsize=12)
        plt.ylabel(f"{numerical_var}", fontsize=12)
        plt.xticks(rotation=45)
        plt.show()

    # Creating dynamic widgets for filtering
    filter_widgets_dict = {
        var: Dropdown(options=df[var].unique(), description=var)
        for var in filter_categories
    }

    # Creating the interactive plot
    interact(_interactive_violinplot, **filter_widgets_dict)


def create_pairplot(
    df: pd.DataFrame,
    numerical_columns: List[str],
):
    """Creates a pairplot of the features.

    Args:
        df (pd.DataFrame): The data used.
        numerical_columns (List[str]): List of numerical features to include in the plot.
    """

    with sns.plotting_context(rc={"axes.labelsize": 16}):
        sns.pairplot(df[numerical_columns], kind="hist")
    plt.show()


def create_correlation_matrix(
    df: pd.DataFrame,
    numerical_columns: List[str],
):
    """Creates a correlation matrix of the features.

    Args:
        df (pd.DataFrame): The data used.
        numerical_columns (List[str]): List of features to include in the plot.
    """
    plt.figure(figsize=(10, 10))
    sns.heatmap(
        df[numerical_columns].corr(),
        square=True,
        annot=True,
        cbar=False,
        cmap="RdBu",
        vmin=-1,
        vmax=1,
    )
    plt.title("Correlation Matrix of Variables")

    plt.show()
