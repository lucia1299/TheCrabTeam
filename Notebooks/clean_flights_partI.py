import pandas as pd

df = pd.read_excel("data\Epstein Flight Logs Master - FINAL FOR DW (2021).csv")

df = df.dropna(subset=["passengers"])

df = df[df["passengers"] != "JE"]

df.to_excel("flights_cleaned.xlsx", index=False)