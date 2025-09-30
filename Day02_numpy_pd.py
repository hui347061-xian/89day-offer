import numpy as np
import pandas as pd

# 模拟 1000 天收益
np.random.seed(42)
returns = np.random.randn(1000) * 0.02
prices = 100 * (1 + returns).cumprod()

df = pd.DataFrame({'price': prices})
df['ret'] = df['price'].pct_change()
df['label'] = (df['ret'].shift(-1) > 0).astype(int)

print(df.head())
print("明日上涨比例:", df['label'].mean())
