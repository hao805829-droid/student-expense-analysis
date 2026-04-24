import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sample_expenses.csv")

print(df.head())

category_summary = df.groupby("category")["amount"].sum()
print(category_summary)

category_summary.plot(kind="bar")
plt.title("Spending by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.tight_layout()
plt.show()
