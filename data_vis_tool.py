import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import tkinter as tk
from tkinter import filedialog

# Function to load dataset
def load_dataset():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select a CSV file", filetypes=[("CSV files", "*.csv")])
    if file_path:
        return pd.read_csv(file_path)
    return None

# Function to display dataset summary
def dataset_summary(df):
    print("Dataset Head:\n", df.head())
    print("\nDataset Info:")
    print(df.info())
    print("\nDataset Description:\n", df.describe())

# Function to generate plots
def generate_plots(df):
    numeric_columns = df.select_dtypes(include=['number']).columns
    categorical_columns = df.select_dtypes(include=['object']).columns
    
    if len(numeric_columns) > 0:
        plt.figure(figsize=(8, 5))
        sns.histplot(df[numeric_columns[0]], bins=30, kde=True)
        plt.title(f'Distribution of {numeric_columns[0]}')
        plt.show()
        
        plt.figure(figsize=(8, 5))
        sns.boxplot(data=df[numeric_columns])
        plt.title('Boxplot of Numeric Features')
        plt.show()
    
    if len(categorical_columns) > 0:
        plt.figure(figsize=(8, 5))
        sns.countplot(x=categorical_columns[0], data=df)
        plt.xticks(rotation=45)
        plt.title(f'Countplot of {categorical_columns[0]}')
        plt.show()

# Function to generate an interactive scatter plot
def interactive_plot(df):
    numeric_columns = df.select_dtypes(include=['number']).columns
    if len(numeric_columns) >= 2:
        fig = px.scatter(df, x=numeric_columns[0], y=numeric_columns[1], color=df.columns[0], title='Interactive Scatter Plot')
        fig.show()

if __name__ == "__main__":
    dataset = load_dataset()
    if dataset is not None:
        dataset_summary(dataset)
        generate_plots(dataset)
        interactive_plot(dataset)
    else:
        print("No dataset loaded. Please select a CSV file.")
