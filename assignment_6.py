
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 1. Load Automobile Dataset from UCI
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df = pd.read_csv(url, header=None, na_values="?")

# Select required columns
df = df[[2, 3, 9, 10, 21, 25]]
df.columns = ['make', 'fuel_type', 'wheel_base',
              'length', 'horsepower', 'price']

print("Original Dataset:")
print(df.head())

# 2. Handle Missing Values
print("\nMissing Values Before:", df.isnull().sum().sum())

for col in ['wheel_base', 'length', 'horsepower', 'price']:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    df[col] = df[col].fillna(df[col].median())

# 3. Encode Categorical Data
df = pd.get_dummies(df, columns=['make', 'fuel_type'],
                    dtype=int)

# 4. Normalize Numerical Data
scaler = MinMaxScaler()

columns = ['wheel_base', 'length', 'horsepower', 'price']
df[columns] = scaler.fit_transform(df[columns])

print("\nPreprocessed Dataset:")
print(df[columns].head().round(2))

print("\nMissing Values After:", df.isnull().sum().sum())
print("Total Rows:", len(df))
