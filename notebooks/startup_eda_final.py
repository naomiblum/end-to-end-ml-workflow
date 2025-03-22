import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

df = pd.read_csv('../data/startup data.csv')
df.shape

df.head()

df.isnull().sum().sort_values(ascending=False).head(20)

df['status'].value_counts().plot(kind='bar', title='Success vs Failure')

df['status_binary'] = df['status'].map({'acquired': 1, 'closed': 0})

numeric_cols = df.select_dtypes(include='number')
plt.figure(figsize=(10, 6))
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')

# Load essential libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

%matplotlib inline

# Load the dataset (update path if needed)
df = pd.read_csv('../data/startup_data.csv')

cat_cols = df.select_dtypes(include='object').columns.tolist()
num_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
print("Categorical columns:", cat_cols)
print("Numerical columns:", num_cols)

for col in cat_cols:
    plt.figure(figsize=(8, 4))
    sns.countplot(data=df, x=col, order=df[col].value_counts().index[:10])
    plt.xticks(rotation=45)
    plt.title(f'Distribution of {col}')
    plt.show()

plt.figure(figsize=(12,8))
sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

sns.boxplot(data=df, x='status', y='funding_total_usd')
plt.title('Funding Distribution by Startup Status')
plt.show()

df['status_binary'] = df['status'].map({'acquired': 1, 'closed': 0})
df['status_binary'].value_counts(normalize=True)


import numpy as np

# Create a new column with log-transformed funding
df['log_funding_total_usd'] = np.log1p(df['funding_total_usd'])

# Visualize the new distribution
plt.figure(figsize=(10, 5))
sns.histplot(df['log_funding_total_usd'], bins=50, kde=True, color='teal')
plt.title("Log-Transformed Funding Total (USD)")
plt.xlabel("log1p(funding_total_usd)")
plt.grid(True)
plt.show()


