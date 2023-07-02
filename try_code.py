import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

#C:\Users\user\Documents\GitHub\MemoryDiary\Intrusions+Diary+-+Daily+summery_26+June+2023_15.17.xlsx

file_name =r'Intrusions+Diary+-+Daily+summery_26+June+2023_15.17.xlsx'

df = pd.read_excel(file_name)
df_amount = df['Amount']
df_dates = df['StartDate'].astype(str).str[:10]

amount_per_day = pd.concat([df_dates, df_amount], axis=1, join='inner')
sum_values = amount_per_day.groupby('StartDate')['Amount'].sum()
amount_dict = sum_values.to_dict()

print(sum_values.iloc[0][:])

# Extract the dates and amounts from the dictionary
#dates = list(amount_dict.keys())
#amounts = list(amount_dict.values())

# Plot the data
#plt.bar(dates, amounts)

# Set the x-axis labels to rotate for better visibility
#plt.xticks(rotation=90)

# Set the axis labels and title
#plt.xlabel('Date')
#plt.ylabel('Amount')
#plt.title('Amount per Day')

# Display the plot
#plt.show()
#date_dict = {date: df[df['Dates'] == date]['Dates'].tolist() for date in df['Dates'].unique()}
#print(df['Dates'].unique())



#xls = pd.ExcelFile(file_name)
#print(xls.sheet_names)