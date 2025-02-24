"""
Creates a sample demographic DataFrame.
For Power BI: Can be used as test data or template.
Output: DataFrame with columns [Fname, Age, Weight, Gender, State, Children, Pets]
Note: This is a static dataset for testing visualizations
"""

import pandas as pd

df = pd.DataFrame({
	'Fname':['Harry','Sally','Paul','Abe','June','Mike','Tom'],
	'Age':[21,34,42,18,24,80,22],
	'Weight': [180, 130, 200, 140, 176, 142, 210],
	'Gender':['M','F','M','M','F','M','M'],
	'State':['Washington','Oregon','California','Washington','Nevada','Texas','Nevada'],
	'Children':[4,1,2,3,0,2,0],
	'Pets':[3,2,2,5,0,1,5]
})

print(df)
