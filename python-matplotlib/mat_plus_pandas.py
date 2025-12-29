import matplotlib.pyplot as plt
import pandas as pd

import numpy as np

df = pd.read_csv("data/phone_stats.csv")

print(df.to_string())
print(df["brand"])
brands_count = df["brand"].value_counts()

plt.barh(brands_count.index, brands_count.values)
plt.xlabel("Brand")
plt.ylabel("Number of Phones")
plt.title("Number of Phones by Brand")
plt.show()
