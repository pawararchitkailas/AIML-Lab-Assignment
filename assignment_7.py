
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Load UCI Auto MPG Dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"

columns = ['mpg', 'cylinders', 'displacement',
           'horsepower', 'weight', 'acceleration',
           'model_year', 'origin', 'car_name']

df = pd.read_csv(url, sep=r'\s+',
                 names=columns, na_values='?')

# 2. Handle Missing Values
df = df.dropna()

# 3. Select Features and Target
X = df[['cylinders', 'displacement', 'horsepower',
        'weight', 'acceleration', 'model_year', 'origin']]
y = df['mpg']

# 4. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Train Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Predict MPG
y_pred = model.predict(X_test)

# 7. Evaluate Model
print("Total Records:", len(df))
print("Mean Absolute Error:",
      round(mean_absolute_error(y_test, y_pred), 2))
print("R2 Score:", round(r2_score(y_test, y_pred), 2))

# 8. Feature Influence
print("\nFeature Coefficients:")
for feature, coefficient in zip(X.columns, model.coef_):
    print(feature, ":", round(coefficient, 4))

# 9. Visualization
plt.scatter(y_test, y_pred, color='blue')
plt.plot([y.min(), y.max()], [y.min(), y.max()],
         color='red', linestyle='--')
plt.xlabel("Actual MPG")
plt.ylabel("Predicted MPG")
plt.title("Actual vs Predicted MPG")
plt.show()
