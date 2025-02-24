import pandas as pd

dataset['num_caracteres'] = dataset['comment_textDisplay'].astype(str).str.len()
