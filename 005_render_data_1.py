"""
Creates a scatter plot of Age vs Weight.
For Power BI: Expects 'dataset' DataFrame with 'Age' and 'Weight' columns.
Note: In Power BI, plt.show() is not needed as Power BI handles the display
"""

import matplotlib.pyplot as plt

dataset.plot(kind='scatter', x='Age', y='Weight', color='red’)

plt.show()
