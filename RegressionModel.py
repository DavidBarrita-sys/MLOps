import pandas as pd

file_path = 'test/OnlineRetail.csv'
data = pd.read_csv(file_path, encoding='ISO-8859-1')


data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'], errors='coerce')

data['TotalSales'] = data['Quantity'] * data['UnitPrice']

latest_year = data['InvoiceDate'].dt.year.max()

filtered_data_latest_year = data[data['InvoiceDate'].dt.year == latest_year]

sales_by_country_latest_year = filtered_data_latest_year.groupby('Country')['TotalSales'].sum().reset_index()

sales_by_country_latest_year_sorted = sales_by_country_latest_year.sort_values(by='TotalSales', ascending=False)

import ace_tools as tools
tools.display_dataframe_to_user(name="Country Sales for Latest Year", dataframe=sales_by_country_latest_year_sorted)

sales_by_country_latest_year_sorted.head()
