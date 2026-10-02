import pandas as pd
import matplotlib.pyplot as plt

# Excel file read karna
file_path = "COVID_19_Global_Impact_Dashboard_Excel.xlsx"

df = pd.read_excel(file_path, sheet_name="Raw_Data")

# Basic information
print("COVID-19 Dataset")
print("----------------")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())

# Missing values check
print("\nMissing Values:")
print(df.isnull().sum())

# Basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Country-wise total cases
country_cases = (
    df.groupby("location")["total_cases"]
    .max()
    .sort_values(ascending=False)
)

print("\nTop Countries by Total Cases:")
print(country_cases.head(10))

# Country-wise total deaths
country_deaths = (
    df.groupby("location")["total_deaths"]
    .max()
    .sort_values(ascending=False)
)

print("\nTop Countries by Total Deaths:")
print(country_deaths.head(10))

# Cases per million
cases_million = (
    df.groupby("location")["total_cases_per_million"]
    .max()
    .sort_values(ascending=False)
)

print("\nTop Countries by Cases per Million:")
print(cases_million.head(10))

# Vaccination analysis
vaccination = (
    df.groupby("location")["people_vaccinated_per_hundred"]
    .max()
    .sort_values(ascending=False)
)

print("\nTop Countries by Vaccination Percentage:")
print(vaccination.head(10))

# New cases trend
if "date" in df.columns and "new_cases" in df.columns:
    df["date"] = pd.to_datetime(df["date"])

    daily_cases = df.groupby("date")["new_cases"].sum()

    plt.figure(figsize=(12, 6))
    plt.plot(daily_cases.index, daily_cases.values)
    plt.title("COVID-19 New Cases Trend")
    plt.xlabel("Date")
    plt.ylabel("New Cases")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

print("\nAnalysis completed successfully!")
