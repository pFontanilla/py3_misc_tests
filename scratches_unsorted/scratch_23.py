import os, sys
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "col1": [1,2],
    "col2": [3,4]
})

print(df.to_string())

df["col3"] = df.apply(lambda row: row.col1 + row.col2, axis=1)

print(df.to_string())