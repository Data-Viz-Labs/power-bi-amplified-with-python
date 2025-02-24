"""
Calculates the length of comments in a text column.
For Power BI: Expects a DataFrame named 'dataset' with column 'comment_textDisplay'.
Input: DataFrame with text comments
Output: Adds 'num_caracteres' column with comment length
Note: Compatible with Power BI's DataFrame handling
"""

import pandas as pd

dataset['num_caracteres'] = dataset['comment_textDisplay'].astype(str).str.len()
