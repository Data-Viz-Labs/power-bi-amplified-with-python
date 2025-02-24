"""
Creates a dual-line chart comparing Pets and Children by Name.
For Power BI: Expects 'dataset' DataFrame with columns 'Fname', 'Children', 'Pets'.
Note: Figure size might need adjustment based on Power BI visual container
"""

import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
ax = plt.gca()

dataset.plot(kind='line',x='Fname',y='Children',ax=ax)
dataset.plot(kind='line',x='Fname',y='Pets', color='red', ax=ax)

plt.show()
