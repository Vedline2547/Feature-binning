# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
# Load dataset
df = pd.read_csv(r"C:\Users\HP\Desktop\New ML\Feature-binning\Churn_Modelling.csv")
# First few rows of dataset
print(df.head())
# Dataset info 
print(df.info())
df.drop(columns=['CustomerId','RowNumber','Surname'],inplace=True)
print(df.head())
print(df.Age.min())
print(df.Age.max())
labels = ['0-20','21-40','41-60','Above 61']
bins = [0,20,40,60,100]
df['Age_bins'] = pd.cut(df.Age,bins,labels=labels,include_lowest=True)
df[['Age','Age_bins']].to_csv('test.csv')
print(df.Age_bins.value_counts())
plt.figure(figsize=(8, 5))
plt.bar(labels,df.Age_bins.value_counts())
plt.title('Customer age distribution')
plt.xlabel('Age Bins')
plt.ylabel('Age Count')
plt.show()