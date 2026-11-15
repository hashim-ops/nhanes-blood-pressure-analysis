import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Research question: How does average systolic blood pressure differ across age groups among NHANES adult participants?

df = pd.read_csv('NHANES_data.csv')

#There actually no samples beyond the age of 80, therefore there's no reason to keep any number >80 in the bins
bins = [17, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
df['AgeRanges'] = pd.cut(df['RIDAGEYR'], bins=bins)

x=df.groupby('AgeRanges')['BPXSY1'].agg(
    ["count", "mean", "median", "std"]
)
print(x)

#Visualization
sns.barplot(
    data=df,
    x='AgeRanges',
    y='BPXSY1'
)
plt.title('Bar Chart of ages and their average Blood Pressure')
plt.xlabel('Age Ranges')
plt.ylabel('Average Blood Pressure')
plt.show()

print(f'Pearsons correlation coefficient: {df['BPXSY1'].corr(df['RIDAGEYR'])})')
