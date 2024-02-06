import pandas as pd

df = pd.read_excel("epstein_flights.xlsx")

df = df.dropna(subset=["passengers"])

df = df[df["passengers"] != "JE"]

df.to_excel("modified_excel_file.xlsx", index=False)