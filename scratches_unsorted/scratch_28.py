import pandas as pd
import numpy as np
import re

regex_split_order_codes = re.compile(r'(.*)(@)(.*)(\(.+\))')

mpn1 = 'MMA02040C1820F@00 (B0/B3/M3)'
mpn2 = 'SBA02040C1820F@ (B0/B3/M3)'
mpn3 = 'holder'
mpn4 = 'FFA02040C1820F@(B0/B3)'
tpn1 = '300-3-00001'
tpn2 = '300-3-00232'
tpn3 = '300-3-00432'
tpn4 = '300-3-00875'

df = pd.DataFrame({'q': [mpn1, mpn2, mpn3, mpn4], 'tpn': [tpn1, tpn2, tpn3, tpn4]})

df_split = df.q.str.extract(regex_split_order_codes)
df_split.columns = ['a', 'b', 'c', 'd']

df_split['code_count'] = df_split.d.str.count('/') + 1
df_split.loc[df_split[df_split.columns[-2]].isna(), 'code_count'] = 1
df_split.loc[df_split.d.isna(), 'd'] = df.q

df_codes = df_split.d.str.strip("()").str.split("/", expand=True).stack().reset_index().drop(['level_0', 'level_1'], axis=1)
df_codes.columns = ['code']

df = df.join(df_split['code_count'])
df = df.reindex(df.index.repeat(df.code_count)).fillna('').drop('code_count', axis=1).reset_index(drop=True)

df_split = df_split.reindex(df_split.index.repeat(df_split.code_count)).fillna('').reset_index(drop=True)
df_split = df_split.join(df_codes)

df['q'] = df_split.a.astype(str) + df_split.code.astype(str) + df_split.c.astype(str)
print(df)