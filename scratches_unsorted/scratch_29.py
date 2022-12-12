import pandas as pd

mpn1 = 'MMA02040C1820F@00 (B0/B3/M3)'
mpn2 = '300-3-00432'
mpn3 = 'holder'
mpn4 = 'FFA02040C1820F@(B0/B3)'
tpn1 = '300-3-00001'
tpn2 = '300-3-00232'
tpn3 = '300-3-00432'
tpn4 = '300-3-00875'
mpns = [mpn1, mpn2, mpn3, mpn4]
tpns = [tpn1, tpn2, tpn3, tpn4]

df = pd.DataFrame({'tpn': tpns, 'q': mpns})

print("*"*20)
print(df)
print("*"*20)
print(df[~df.q.isin(df.tpn)])
print("*"*20)
