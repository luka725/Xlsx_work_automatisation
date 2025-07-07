import pandas as pd
import openpyxl as px
import numpy as np

# loading excel file sheet1
# Note: The sheet_name parameter is 1, which refers to the second sheet in the Excel file.

pd.set_option('display.max_rows', None)  # Setting option to display all rows
df = pd.read_excel("./data/sruli.xlsx", sheet_name = 1, header = 1)
df.columns = [col.replace(' ', '_') for col in df.columns]  # Stripping whitespace from column names

amount = df["Amount"]

df["new_date"] = pd.to_datetime(df["Date"], errors='coerce')  # Converting 'Date' column to datetime
df["Ang_debeti"] = np.where(df["Amount"] < 0, df["Op._Code"], df["Account_Number"])
df["Ang_krediti"] = np.where(df["Amount"] > 0, df["Op._Code"], df["Account_Number"])
df["work_currency"] = df["Currency"]
df["NBG_rate"] = np.where(df["work_currency"] == "GEL", 1, np.where(df["work_currency"] == "USD", 2, 3))
df["money_val_debit"] = np.where(df["Amount"] > 0, df["Amount"], 0)
df["money_val_credit"]= np.where(df["Amount"] < 0, df["Amount"] *-1, 0)
df["new_description"] = df["Description"]
df["eqv_lari_debeti"] = df["money_val_debit"] * df["NBG_rate"]
df["eqv_lari_krediti"] = df["money_val_credit"] * df["NBG_rate"]

df.to_excel("./data/sruli_chemi_namushevari.xlsx", index=False)  # Saving the modified DataFrame back to Excel

print(type(amount[1]))  # Displaying the column names of the dataframe
print(df["Ang_debeti"])  # Displaying the Ang_debeti column
print(df["Ang_krediti"])  # Displaying the Ang_krediti column
print(df["work_currency"])  # Displaying the work_currency column
print(df["money_val_debit"])  # Displaying the money_val_debit column
print(df["money_val_credit"])  # Displaying the money_val_credit column
print(df["new_description"])  # Displaying the new_description column
print(df["new_date"])  # Displaying the new_date column
print(df["NBG_rate"])  # Displaying the NBG_rate column
print(df["eqv_lari_debeti"])  # Displaying the eqv_lari_debeti column
print(df["eqv_lari_krediti"])  # Displaying the eqv_l
