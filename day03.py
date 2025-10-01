import pandas as pd

# 模拟 3 天数据
data = {
    'date': ['2025-01-01', '2025-01-02', '2025-01-03'],
    'price': [100.0, 101.2, 99.8],
    'ret': [None, 0.012, -0.014],
    'label': [None, 1, 0]
}
df = pd.DataFrame(data)
df['ret'] = df['price'].pct_change()
df['label'] = (df['ret'].shift(-1) > 0).astype(int)

print(df)
print("明日上涨比例：", df['label'].mean())
