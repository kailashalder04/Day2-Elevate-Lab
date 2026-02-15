
# TITANIC DATASET - COMPLETE EDA


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

OUTPUT_DIR = "eda_outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load Dataset


df = pd.read_csv(r"E:\New folder (3)\OneDrive\Desktop\Elevate Labs\Day1\Data\Titanic-Dataset.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())


# Summary Statistics


print("\nSummary Statistics:")
print(df.describe())

print("\nMedian Values:")
print(df.median(numeric_only=True))


# Missing Values


print("\nMissing Values:")
print(df.isnull().sum())


# Histograms for Numeric Features


numeric_cols = df.select_dtypes(include=np.number).columns

for col in numeric_cols:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col], kde=True)
    plt.title(f"Histogram of {col}")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f"hist_{col}.png"))
    plt.close()


# Boxplots (Outlier Detection)


for col in numeric_cols:
    plt.figure(figsize=(6,4))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f"box_{col}.png"))
    plt.close()


# Correlation Matrix


plt.figure(figsize=(10,8))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.savefig(os.path.join(OUTPUT_DIR, "correlation_matrix.png"))
plt.close()


# Pairplot (Feature Relationships)


sns.pairplot(df[['Survived','Pclass','Age','Fare']], hue='Survived')
plt.show()


# Survival Analysis


# Survival count
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.savefig(os.path.join(OUTPUT_DIR, "survival_count.png"))
plt.close()

# Survival by Gender
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival by Gender")
plt.show()

# Survival by Passenger Class
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival by Class")
plt.show()


# Plotly Interactive Visualization


fig = px.histogram(df, x="Age", color="Survived",
                   title="Age Distribution by Survival",
                   marginal="box")
fig.write_html(os.path.join(OUTPUT_DIR, "age_survival_plot.html"))


# Basic Inferences


print("\nKey Observations:")
print("1. Females had higher survival rate than males.")
print("2. First class passengers had better survival chances.")
print("3. Fare is positively correlated with survival.")
print("4. Age shows slight variation but not strong predictor alone.")
print("5. Some features show skewness (Fare).")

print("\nEDA Completed Successfully.")
