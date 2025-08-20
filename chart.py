import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -------------------------------
# Generate Synthetic Data
# -------------------------------
np.random.seed(42)
categories = ["Electronics", "Clothing", "Home & Kitchen", "Sports", "Beauty", "Toys"]
satisfaction_scores = [np.random.normal(loc=7 + i*0.3, scale=0.5, size=100) for i in range(len(categories))]

# Create DataFrame
data = pd.DataFrame({
    "Category": np.repeat(categories, 100),
    "Satisfaction": np.concatenate(satisfaction_scores)
})

# -------------------------------
# Create Visualization
# -------------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

plt.figure(figsize=(8, 8))  # 8x8 inches * 64 dpi = 512x512

ax = sns.barplot(
    data=data,
    x="Category",
    y="Satisfaction",
    hue="Category",
    legend=False,
    palette="viridis",
    errorbar="ci"
)

ax.set_title("Average Customer Satisfaction by Product Category", fontsize=16, pad=20)
ax.set_xlabel("Product Category", fontsize=14)
ax.set_ylabel("Average Satisfaction Score", fontsize=14)
ax.set_ylim(0, 10)

plt.xticks(rotation=30, ha="right")
sns.despine()

# -------------------------------
# Save Chart (EXACT 512x512)
# -------------------------------
plt.savefig("chart.png", dpi=64, bbox_inches=None)  # ✅ keeps 512x512 exact
plt.close()