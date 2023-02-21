import pandas as pd

df =pd.read_table('dist.txt', 
         delim_whitespace=True,
                  names=('A', 'B', 'C'))
print(df)

print("#################################")
print("#################")
data = pd.read_csv('dist.txt', delimiter= '\s+',
                   header=None, index_col=False)