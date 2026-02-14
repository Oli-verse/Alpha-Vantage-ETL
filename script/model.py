import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split    
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('IBM_monthly_data.csv')


df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

df['Target_Next_Month_Close'] = df['Close'].shift(-1)

df['SMA_3'] = df['Close'].rolling(window=3).mean()

df_ml = df.dropna().copy()

features = ['Open', 'High', 'Low', 'Close', 'Volume', 'SMA_3']
X = df_ml[features]

y = df_ml['Target_Next_Month_Close']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
r2 = r2_score(y_test, predictions)
mse = mean_squared_error(y_test, predictions)

print(f"--- Model Results ---")
print(f"R-Squared Score: {r2:.4f}")
print(f"Mean Squared Error: {mse:.4f}")

plt.figure(figsize=(10, 6))
plt.scatter(y_test, predictions, alpha=0.5, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Next Month Price')
plt.ylabel('Predicted Next Month Price')
plt.title('Actual vs Predicted IBM Stock Prices')

plt.savefig('IBM_prediction_results.png', dpi=300, bbox_inches='tight')
print("Figure saved as 'IBM_prediction_results.png'")

plt.show()

a