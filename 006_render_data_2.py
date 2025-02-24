"""
Creates a bar chart of Age by First Name.
For Power BI: Expects 'dataset' DataFrame with 'Fname' and 'Age' columns.
Note: Matplotlib figure will be automatically captured by Power BI
"""

import matplotlib.pyplot as plt
dataset.plot(kind='bar',x='Fname',y='Age')

plt.show()
