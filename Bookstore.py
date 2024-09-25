# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C3TEhKXVhK2kf1-BTgdfwTwsjMVTtGde
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

x=pd.read_csv("Project Cleaning and Formatting of Phone Numbers - Customers_books_purchases.csv")

x.head(2)

x.info()

a=x.columns

for i in a:
  if x[i].isnull().sum()>0:
    print(i," has",x[i].isnull().sum()," null values")
  else:
    pass

for i in a:
  if x[i].isnull().sum()>0:
    print(i," has",x[i].dtype, "data type")
  else:
    pass

# x=data[data["Email"].apply(lambda x: type(x)==str)]

# print(x["Email"].apply(type).value_counts())

# print(x["Email"].apply(lambda x: np.nan if type(x)==int else x).value_counts())

# x["Email"].apply(type).value_counts()



# x["Email"].dropna()

# x["Email"].str

# x["Email"].astype(str).inplace=True

# x["Email"].apply(lambda x: x.drop if type(x)!=str else x)

x["Email"].dropna()

x["Email"].astype(str)

# prompt: drop rows when a smae emails occour for more than 1 time

x = x.drop_duplicates('Email', keep=False)

x["Email"].value_counts()

x.head()

x["Address"]

# prompt: extract pincode out of x[address] and put in column x["Pincode"]

import re

def extract_pincode(address):
  """Extracts the pincode from an address string."""
  if isinstance(address, str):
    pincode_match = re.search(r'\b\d{5}\b', address)  # Matches 5 consecutive digits
    if pincode_match:
      return pincode_match.group(0)
  return None

x["Pincode"] = x["Address"].apply(extract_pincode)

x["Pincode"].nunique()

x.head()

x["PurchaseAmount"].astype(int)

x["Phone"]

x["New_Phone"]=x["Phone"].dropna()

# prompt: drop null values in x["New_Phone"]

x.dropna(subset=["New_Phone"], inplace=True)

x["New_Phone"].isnull().sum()

x.astype({"New_Phone":int})

x["Phone"]=x["New_Phone"]

x.drop("New_Phone",axis=1,inplace=True)

x.info()

a=x.columns
for i in a:
  x.dropna(subset=[i], inplace=True)

a=x.columns
for i in a:
  if x[i].isnull().sum()>0:
    print(i," has",x[i].isnull().sum()," null values")
  else:
    print("No Null values")

x["PurchaseAmount"]=x["PurchaseAmount"].astype(int)

# prompt: convert x["PurchaseDate"] to date and in same format

from datetime import datetime

def convert_to_date(date_str):
  try:
    return datetime.strptime(date_str, '%d-%m-%Y').strftime('%Y-%m-%d')
  except ValueError:
    return None

x['PurchaseDate'] = x['PurchaseDate'].apply(convert_to_date)

med=x["PurchaseDate"].mode()

med.dtype

x["PurchaseDate"].head(5)

pd.set_option("display.max_rows",None)
x["PurchaseDate"].fillna(med, inplace=True)

x["PurchaseDate"] = pd.to_datetime(x["PurchaseDate"], format='%Y-%m-%d', errors='coerce')

print(x["PurchaseDate"].head())

med = x["PurchaseDate"].mode()[0]

x["PurchaseDate"].fillna(med, inplace=True)

print(x["PurchaseDate"].head())

x.info()

x['Pincode'] = x['Pincode'].astype(float).astype(int)

x["Pincode"].isnull().sum()

print(x['Pincode'].dtype)

x['Phone'] = x['Phone'].astype(float).astype(int)

x["Phone"].isnull().sum()

print(x['Phone'].dtype)

x.info()

a=x.columns
for i in a:
  print(i," has",x[i].nunique()," unique values")

sns.pointplot(x="PurchaseDate",y="PurchaseAmount",data=x,color="blue",linewidth=1)
plt.show()

plt.hist(x["PurchaseAmount"], bins=10, color="blue", alpha=0.7)

# Apply the rainbow colormap
plt.hist(x["PurchaseAmount"], bins=10, color=plt.cm.rainbow(np.linspace(0, 1, 10)))

plt.title("Histogram of Purchase Amounts")
plt.xlabel("Purchase Amount")
plt.ylabel("Frequency")
plt.show()

sns.boxplot(data=x,x="PurchaseAmount",color="green")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

# Combine scatter plot with kdeplot to show individual points
sns.scatterplot(x=x["CustomerID"], y=x["PurchaseAmount"], color="purple", alpha=0.5)
sns.kdeplot(x=x["CustomerID"], y=x["PurchaseAmount"], cmap="coolwarm", fill=True, thresh=0.05)

# Customize the plot
plt.title("Pair Plot for Outlier Detection")
plt.xlabel("CustomerID")
plt.ylabel("PurchaseAmount")

plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Assuming 'x' is your DataFrame and using the IQR method for outlier detection
# Calculate Q1 (25th percentile) and Q3 (75th percentile) for PurchaseAmount
Q1 = x["PurchaseAmount"].quantile(0.25)
Q3 = x["PurchaseAmount"].quantile(0.75)
IQR = Q3 - Q1  # Interquartile Range

# Define bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Detect outliers
outliers = x[(x["PurchaseAmount"] < lower_bound) | (x["PurchaseAmount"] > upper_bound)]
non_outliers = x[(x["PurchaseAmount"] >= lower_bound) & (x["PurchaseAmount"] <= upper_bound)]

# Plotting
plt.figure(figsize=(10,6))

# Plot non-outliers as a scatter plot
sns.scatterplot(x=non_outliers["CustomerID"], y=non_outliers["PurchaseAmount"], color="blue", label="Non-outliers", alpha=0.5)

# Plot outliers as red points
sns.scatterplot(x=outliers["CustomerID"], y=outliers["PurchaseAmount"], color="red", label="Outliers", s=100)

# Customize the plot
plt.title("Outlier Detection using IQR")
plt.xlabel("CustomerID")
plt.ylabel("PurchaseAmount")
plt.legend()

# Show the plot
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Assuming 'x' is your DataFrame and using the IQR method for outlier detection
# Calculate Q1 (25th percentile) and Q3 (75th percentile) for PurchaseAmount
Q1 = x["PurchaseAmount"].quantile(0.40)
Q3 = x["PurchaseAmount"].quantile(0.60)
IQR = Q3 - Q1  # Interquartile Range

# Define bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Detect outliers
outliers = x[(x["PurchaseAmount"] < lower_bound) | (x["PurchaseAmount"] > upper_bound)]
non_outliers = x[(x["PurchaseAmount"] >= lower_bound) & (x["PurchaseAmount"] <= upper_bound)]

# Plotting
plt.figure(figsize=(10,6))

# Plot non-outliers as a scatter plot
sns.scatterplot(x=non_outliers["CustomerID"], y=non_outliers["PurchaseAmount"], color="blue", label="Non-outliers", alpha=0.5)

# Plot outliers as red points
sns.scatterplot(x=outliers["CustomerID"], y=outliers["PurchaseAmount"], color="red", label="Outliers", s=100)

# Annotate outlier points with their values
# for i in range(outliers.shape[0]):
#     plt.text(outliers["CustomerID"].iloc[i], outliers["PurchaseAmount"].iloc[i],
#              f'{outliers["PurchaseAmount"].iloc[i]:.2f}',
#              color='black', fontsize=9, weight='bold')

# Customize the plot
plt.title("Outlier Detection using IQR")
plt.xlabel("CustomerID")
plt.ylabel("PurchaseAmount")
plt.legend()

# Show the plot
plt.show()

