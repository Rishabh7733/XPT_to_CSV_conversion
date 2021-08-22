import pandas 
df = pandas.read_sas('xpt file path', format=None, index=None, encoding=None, chunksize=None, iterator=False)
#print(df)
cols = list(df.columns)


# 87 - rows
# 37 - col
for col_name in cols:
    df1 = df[col_name]
    k = []
    for i in range(0,87):
        d = str(df1[i])
        k.append(d)
    df[col_name] = k
#print(df)

df.to_csv (r'D:/ae_4May.csv', index = False, header=True)