import pandas as pd
df = pd.read_csv('data1.csv')
# # SALE มากกว่า 0
df1 = df[df['SALE']>0]
print(df1)

# # Sale มี 0
df2 = df
print(df2)



