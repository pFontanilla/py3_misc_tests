import functools
import pandas as pd
import numpy as np

frame1 = pd.DataFrame(
    {
        "ID": [1,2,3,4,5],
        "Name":["John", "Sam", "Frank", "John", "Bill"]
    },
)
frame2 = pd.DataFrame(
    {
        "ID": [1,6,2],
        "Name":["John", "Hamilton", "Tim"]
    },
)

print(frame1)
print("\n")
print(frame2)
print("\n")
print(frame1.isin(frame2))
print("\n")
print(frame1["ID"].isin(frame2["ID"]))
print("\n")
print(frame1[frame1["ID"].isin(frame2["ID"])])
print("\n")
print(frame2[~frame2["ID"].isin(frame1["ID"])])