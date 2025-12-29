import pandas as pd

df = pd.read_csv('data/phone_stats.csv')

print(df)
print(df.to_string())

# df = pd.read_json('data/phone_stats.json')
# print(df)
# print(df.to_string())

# Selection by column

print(df['brand'].to_string())

print(df['rating'].to_string())

print(df[['brand', 'rating', 'price_usd']].to_string())

# Selection by row
print(df.to_string())

print(df.loc[1].to_string())


print(df.iloc[0:3].to_string())
print(df.iloc[0].to_string())

print(df.loc[0:3, ['brand', 'rating', 'price_usd']].to_string())

# Filtering
print(df[df['brand'] == 'Apple'].to_string())
print(df[df['price_usd'] > 700].to_string())
print(df[(df['brand'] == 'Apple') & (df['price_usd'] > 700)].to_string())
print(df[(df['brand'] == 'Apple') | (df['price_usd'] > 700)].to_string())

df_a = pd.read_csv('data/phone_stats.csv', index_col="brand")
print(df_a.to_string())
print(df_a.loc['Motorola'].to_string())

# Sorting
print(df.sort_values(by='price_usd').to_string())
print(df.sort_values(by='price_usd', ascending=False).to_string())
print(df.sort_values(by=['brand', 'price_usd']).to_string())
print(df.sort_values(by=['brand', 'price_usd'], ascending=[True, False]).to_string())

# Adding new column
df['in_stock'] = [True, True, False, True, False, True]
print(df.to_string())
# Modifying existing column
df['price_usd'] = df['price_usd'] * 1.1
print(df.to_string())


# Deleting column

df.drop(columns=['screen_size_inches'], inplace=True)
# drop row where ram_gb is less than 6 using drop
df.drop(df[df['ram_gb'] < 6].index, inplace=True)

print(df.to_string())

# aggregation
print(df.sum(numeric_only=True).to_string())
print(df['price_usd'].mean())
print(df['rating'].max())
print(df['rating'].min())
print(df['price_usd'].sum())
print(df['brand'].nunique())

# Grouping
print(df.to_string())
grouped = df.groupby('brand')
print(grouped['rating'].count().to_string())
print(grouped['price_usd'].mean().to_string())
print(grouped['rating'].max().to_string())

# data cleanup
