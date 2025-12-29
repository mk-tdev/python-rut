import pandas as pd

data = [100, 102, 104, 106, 108]

series = pd.Series(data, index=('A', 'B', 'C', 'D', 'E'))

print(series)

series.loc['A'] = 200

series.loc['A']

series.iloc[2]

print(series[series > 105])

