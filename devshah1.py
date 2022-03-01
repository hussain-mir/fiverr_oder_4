import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\FTC\Desktop\oder_4\danielle_ed_actively.csv")

sns.countplot(x='action', data=df)

df['date']=pd.to_datetime(df['date'])
df['date'].dt.date


ts=input('Enter start date')
ts1=input('Enter Last date')


df3=df.loc[(df['date']>ts)&(df['date']<ts1)]

sns.countplot(x='action',data=df3)
plt.show()
