import pandas as pd
import openpyxl as px

# loading excel file sheet1
df = pd.read_excel("./data/my excel.xlsx", sheet_name = 1, header = 1)

df.columns = [col.replace(' ', '_') for col in df.columns]  # Stripping whitespace from column names

#dropping unnecessary columns
df = df.drop(['Balance', 'Document_Date', 'Document_Number', "Partner's_Bank", 'Intermediary_Bank_Code', 
            'Intermediary_Bank', 'Charge_Details', 'Taxpayer_Name', 'Treasury_Code', 'Additional_Description'], axis=1)


for index, row in df.iterrows():
    row = row.fillna(0)  # Fill NaN values with 0

df.to_excel("./data/my excel.xlsx", index=False, sheet_name='Sheet1')