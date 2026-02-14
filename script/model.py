import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('IBM_monthly_data.csv')


df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df = df.sort_values('Date')
df['Returns'] = df['Close'].pct_change()
df = df.dropna()  

sns.regplot(data=df, x='Volume', y='Returns', scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Volume vs. Returns (Predictive Relationship)')
plt.xlabel('Trading Volume')
plt.ylabel('Monthly Returns (%)')
plt.savefig('volume_vs_returns_scatter.png')
plt.show()


print(f"Correlation between Volume and Returns: {df['Volume'].corr(df['Returns']):.4f}")