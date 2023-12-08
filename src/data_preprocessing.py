#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import csv

# Load the Excel file into a Pandas DataFrame
excel_file = 'data_raw/raw_healthCare_data.xlsx' 
data = pd.read_excel(excel_file)

# Save the DataFrame to a CSV file
csv_file = 'data_raw/raw_healthCare_data.csv' 
data.to_csv(csv_file, index=False, encoding='utf-8-sig')  # Set index=False to avoid writing row indices


# Load the CSV file into a pandas DataFrame with the specified encoding
file_path = 'data_raw/raw_healthCare_data.csv'
encoding = 'utf-8-sig'
df_health = pd.read_csv(file_path, encoding=encoding)

df_health = df_health.replace('’', "'", regex=True)
df_health.to_csv(csv_file, index=False, encoding='utf-8')

print(df_health.head())

# Count and print the missing values before replacement with NA
missing_values = df_health.isna().sum()
print("Missing values before replacement:")
print(missing_values)

# Replace missing values with "NA"
df_health.fillna("NA", inplace=True)

# Count and print the missing values after replacement with NA
missing_values_after = df_health.isna().sum()
print("Missing values after replacement:")
print(missing_values_after)

# Remove leading and trailing spaces from object columns using str.strip() function
df_health_obj = df_health.select_dtypes(['object'])
df_health[df_health_obj.columns] = df_health_obj.apply(lambda x: x.str.strip())

# Renamimg the columns with the meaningful names
df_health.rename(columns={'Hospital Name': 'hospital_name',
                   'Hospital Type ': 'hospital_type',
                   'Postal Code': 'postal_code',
                   "Doctor's Name": 'doctor_name',
                   'Facility Type ': 'facility_type',
                    'Emergency Service' : 'emergency_services',
                    'Opening Hours' : 'opening_hours',
                    'Web site URL' : 'website_url'}, inplace=True)
print(df_health.head())

# Save the cleaned DataFrame directly to a new CSV file
output_file = 'data_clean/clean_healthCare_data.csv'
df_health.to_csv(output_file, index=False, sep=',', quoting=csv.QUOTE_MINIMAL, quotechar='"', escapechar='\\', encoding='utf-8-sig')

print(f"Cleaned data saved to {output_file}")
     


# In[ ]:




