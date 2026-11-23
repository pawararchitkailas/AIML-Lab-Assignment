
import statistics

# Arithmetic Operations
a = 20
b = 10

print("Arithmetic Operations:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Statistical Operations
data = [10, 20, 30, 40, 50]

print("\nStatistical Operations:")
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))
print("Standard Deviation:", round(statistics.stdev(data), 2))
print("Variance:", statistics.variance(data))
