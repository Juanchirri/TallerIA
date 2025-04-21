import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())