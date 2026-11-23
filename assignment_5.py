
import math
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Math Library
print("Math Library:")
print("Square Root:", math.sqrt(25))
print("Factorial:", math.factorial(5))

# 2. NumPy Library
data = np.array([10, 20, 30, 40, 50])
print("\nNumPy Library:")
print("Mean:", np.mean(data))
print("Sum:", np.sum(data))

# 3. SciPy Library
print("\nSciPy Library:")
print("Mode:", stats.mode([1, 2, 2, 3], keepdims=False).mode)
print("Standard Error:", round(stats.sem(data), 2))

# 4. Pandas Library
df = pd.DataFrame({
    'Student': ['A', 'B', 'C', 'D', 'E'],
    'Marks': [10, 20, 30, 40, 50]
})

print("\nPandas DataFrame:")
print(df)
print("Average Marks:", df['Marks'].mean())

# 5. Matplotlib Visualization
plt.plot(df['Student'], df['Marks'], marker='o')
plt.title("Student Marks - Matplotlib")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()

# 6. Seaborn Visualization
sns.barplot(data=df, x='Student', y='Marks')
plt.title("Student Marks - Seaborn")
plt.show()
