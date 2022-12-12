import pandas as pd

data = [
    ["VISHAY/BEYSCHLAG", "Approved"]
]

columns = ["Manufacturer", "Approval"]

df = pd.DataFrame(data, columns=columns)
df.to_parquet("MFRs.parquet", engine="fastparquet", compression=None)

print df

dfREAD = pd.read_parquet("MFRs.parquet", engine="fastparquet")

print dfREAD

# print df.parquet

# print df
#
# encrypted = fermet.encrypt("df.parquet")
#
# print encrypted

