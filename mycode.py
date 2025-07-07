import pandas as pd

#loading excel file sheet1
dataframe = pd.read_excel("./data/accounting_sample.xlsx", sheet_name="Sheet1")

# Displaying the column names of the dataframe
for index, row in dataframe.iterrows():
    if row["Amount"] < 0:
        dataframe.at[index, "Amount"] = row["Amount"] * -1

dataframe["Discount"] = dataframe["Amount"] * 0.1

dataframe["Discounted amount"] = dataframe["Discount"] * (dataframe["Amount"]/100)

dataframe.drop(columns=["Date"], inplace=True)

dataframe.to_excel("./data/accounting_sample.xlsx", index=False)

p
