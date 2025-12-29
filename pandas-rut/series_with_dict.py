import pandas as pd

calories = {
    "day1": 420,
    "day2": 380,
    "day3": 390
}

series = pd.Series(calories)
print(series)

series.loc["day2"] = 400

print(series.loc["day2"])

print(series[series > 400])