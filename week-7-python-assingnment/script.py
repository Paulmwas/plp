# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    print("Dataset loaded successfully.")
except Exception as e:
    print("Error loading dataset:", e)

# Display first few rows
print("\nFirst 5 rows:")
print(df.head())

# Check data types and missing values
print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# Clean data (no missing values in this case)
# If there were: df = df.dropna() or df.fillna(...)

# Task 2: Basic Data Analysis
print("\nDescriptive Statistics:")
print(df.describe())

# Group by species and compute mean
grouped_means = df.groupby('species').mean()
print("\nMean of numerical columns grouped by species:")
print(grouped_means)

# Observations
print("\nObservation: Iris-virginica seems to have the highest average petal length and width.")

# Task 3: Visualizations
sns.set(style="whitegrid")

# 1. Line chart (simulate trend by plotting cumulative average of sepal length)
df['index'] = df.index
df['cumulative_sepal_length'] = df['sepal length (cm)'].expanding().mean()

plt.figure(figsize=(8, 5))
plt.plot(df['index'], df['cumulative_sepal_length'], label="Cumulative Sepal Length")
plt.title("Line Chart: Cumulative Average Sepal Length")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.tight_layout()
plt.show()

# 2. Bar chart: Average petal length per species
plt.figure(figsize=(6, 4))
sns.barplot(x='species', y='petal length (cm)', data=df, estimator='mean', ci=None)
plt.title("Bar Chart: Avg Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Avg Petal Length (cm)")
plt.tight_layout()
plt.show()

# 3. Histogram: Distribution of sepal width
plt.figure(figsize=(6, 4))
sns.histplot(df['sepal width (cm)'], kde=True, bins=15)
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 4. Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(6, 4))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title("Scatter Plot: Sepal vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.tight_layout()
plt.show()
