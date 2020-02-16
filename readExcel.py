import pandas as pd
df = pd.read_excel(open("data.xlsx", 'rb'),sheet_name='Sheet1')
a = df.to_dict('records')
print(a)
# r=2
# for i in range(r):
#     print(i)
#     r+ = 2
# r = 0
# output=[]
# for i in data:
#     out = data.iloc[r:r+2].tolist()
#     output.append(out)
#     r+=2