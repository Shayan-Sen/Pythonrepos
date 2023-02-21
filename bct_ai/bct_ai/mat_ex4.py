import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("player_data.csv")
ronaldo_scores=df.iloc[0,1:]
messi_scores=df.iloc[1,1:]
col_names=df.columns[1:]
cols=['green','red','blue']

plt.subplot(1,2,1)
plt.pie(ronaldo_scores,labels=col_names,
        colors=cols,autopct="%.2f%%")
plt.title("Ronaldo")

plt.subplot(1,2,2)
plt.pie(messi_scores,labels=col_names,colors=cols,
        autopct="%.2f%%")
plt.title("Messi")
plt.show()
