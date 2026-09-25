"""
Region Performance — Veda Technology Internship (Data Analytics Track)
Compares sales and profit across regions.

Input : superstore.csv (must contain 'Region', 'Sales', 'Profit' columns)
Output: region_summary.csv, region_performance_chart.png
"""

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# 1. Load
df = pd.read_csv("superstore.csv", encoding="latin1")

# 2. Group by region: total sales, total profit, profit margin, line-item count
summary = (
    df.groupby("Region")
    .agg(Total_Sales=("Sales", "sum"),
         Total_Profit=("Profit", "sum"),
         Line_Items=("Sales", "count"))
    .reset_index()
)
summary["Profit_Margin_%"] = (summary["Total_Profit"] / summary["Total_Sales"] * 100).round(2)

# 3. Rank regions (by sales, and separately by profit margin)
summary["Rank_by_Sales"] = summary["Total_Sales"].rank(ascending=False).astype(int)
summary["Rank_by_Margin"] = summary["Profit_Margin_%"].rank(ascending=False).astype(int)
summary = summary.sort_values("Total_Sales", ascending=False).reset_index(drop=True)

summary.to_csv("region_summary.csv", index=False)
print(summary.to_string(index=False))

# 4. Bar chart: Sales vs Profit by region
x = np.arange(len(summary))
width = 0.35
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.bar(x - width/2, summary["Total_Sales"], width, label="Sales", color="#1F4E78")
ax.bar(x + width/2, summary["Total_Profit"], width, label="Profit", color="#F2A20C")
ax.set_title("Region Performance: Sales vs Profit", fontsize=13, fontweight="bold")
ax.set_ylabel("Amount ($)")
ax.set_xticks(x)
ax.set_xticklabels(summary["Region"])
ax.legend()
ax.grid(True, alpha=0.3, axis="y")
plt.tight_layout()
plt.savefig("region_performance_chart.png", dpi=150)
print("\nSaved: region_summary.csv, region_performance_chart.png")
