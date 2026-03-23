import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("retail_large_dataset (1).csv")

print(df.head())

# Histogram
plt.hist(df['product_price'])
plt.title("Product Price Distribution")
plt.show()

# Boxplot
sns.boxplot(x=df['product_price'])
plt.title("Boxplot of Product Price")
plt.show()

# Heatmap (FIXED)
numeric_df = df.select_dtypes(include=['number'])
sns.heatmap(numeric_df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()