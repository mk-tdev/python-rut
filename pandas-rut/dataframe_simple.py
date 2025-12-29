import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])

print(df)

print(df.loc['b'])

df.loc['b', 'Age'] = 28

print(df.loc['b'])
print(df)

# add a new column
df['Occupation'] = ['Engineer', 'Doctor', 'Artist', 'Lawyer']
print(df)

# add a new row
new_row = pd.DataFrame(
  [
    {'Name': ['Eve'], 'Age': [29], 'City': ['Phoenix'], 'Occupation': ['Scientist']},
    {'Name': ['Frank'], 'Age': 33, 'City': 'Miami', 'Occupation': 'Chef'}
  ],
  index=['e', 'f']
)

df = pd.concat([df, new_row])
print(df)

df.loc['e', 'City'] = 'San Francisco'
df.loc['e', 'Occupation'] = 'Scientist'
df.loc['e', 'Age'] = 30
df.loc['e', 'Name'] = 'Eve'
print(df.loc['e'])
print(df)
