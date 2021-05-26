import pandas
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

data = pandas.read_csv('athlete_data.csv')

season_map = {"womens-basketball": ["Winter"],
              "cross-country": ["Fall"],
              "womens-fencing": ["Winter"],
              "mens-fencing": ["Winter"],
              "field-hockey": ["Fall"],
              "womens-golf": ["Fall", "Spring"],
              "mens-golf": ["Fall", "Spring"],
              "womens-ice-hockey": ["Winter"],
              "mens-ice-hockey": ["Winter"],
              "womens-lacrosse": ["Spring"],
              "mens-lacrosse": ["Spring"],
              "womens-rugby": ["Fall"],
              "alpine-skiing": ["Winter"],
              "mens-soccer": ["Fall"],
              "softball": ["Spring"],
              "womens-swimming-and-diving": ["Winter"],
              "mens-tennis": ["Fall", "Spring"],
              "track-and-field": ["Winter", "Spring"],
              "womens-volleyball": ["Fall"],
              "mens-volleyball": ["Spring"],
              "womens-water-polo": ["Spring"],
              "mens-water-polo": ["Fall"],
              "baseball": ["Spring"],
              "football": ["Fall"],
              "wrestling": ["Winter"],
              "womens-heavyweight-rowing": ["Fall", "Spring"],
              "mens-heavyweight-rowing": ["Fall", "Spring"],
              "womens-lightweight-rowing": ["Fall", "Spring"],
              "mens-lightweight-rowing": ["Fall", "Spring"],
              "mens-sailing": ["Fall", "Spring"],
              "womens-soccer": ["Fall"],
              "womens-squash": ["Winter"],
              "mens-squash": ["Winter"],
              "mens-swimming-and-diving": ["Winter"],
              "womens-tennis": ["Fall", "Spring"],
              "mens-basketball": ["Winter"]}

gender_map = {"mens-basketball": "Men's Sport",
              "womens-tennis": "Women's Sport",
              "womens-lacrosse": "Women's Sport",
              "baseball": "Men's Sport",
              "football": "Men's Sport",
              "womens-soccer": "Women's Sport",
              "mens-water-polo": "Men's Sport",
              "womens-golf": "Women's Sport",
              "womens-squash": "Women's Sport",
              "mens-volleyball": "Men's Sport",
              "mens-ice-hockey": "Men's Sport",
              "mens-soccer": "Men's Sport",
              "womens-basketball": "Women's Sport",
              "womens-rugby": "Women's Sport",
              "track-and-field": "Co-ed Sport",
              "womens-heavyweight-rowing": "Women's Sport",
              "mens-fencing": "Men's Sport",
              "womens-swimming-and-diving": "Women's Sport",
              "wrestling": "Men's Sport",
              "womens-lightweight-rowing": "Women's Sport",
              "mens-sailing": "Men's Sport",
              "cross-country": "Co-ed Sport",
              "womens-fencing": "Women's Sport",
              "mens-lightweight-rowing": "Men's Sport",
              "mens-squash": "Men's Sport",
              "mens-swimming-and-diving": "Men's Sport",
              "womens-volleyball": "Women's Sport",
              "womens-water-polo": "Women's Sport",
              "alpine-skiing": "Co-ed Sport",
              "mens-lacrosse": "Men's Sport",
              "softball": "Women's Sport",
              "mens-tennis": "Men's Sport",
              "mens-heavyweight-rowing": "Men's Sport",
              "field-hockey": "Women's Sport",
              "mens-golf": "Men's Sport",
              "womens-ice-hockey": "Women's Sport"}

grade_map = {
    1: "First-year",
    2: "Sophomore",
    3: "Junior",
    42: 'Red-shirt'
}

print(data[["Sport", "Fall", "Spring"]].groupby(
    "Sport").mean().sort_values(by=["Fall", "Spring"]))
print(data[["Grade", "Fall", "Spring"]].groupby(
    "Grade").mean().sort_values(by=["Fall", "Spring"]))
print(data[["Gender", "Fall", "Spring"]].groupby(
    "Gender").mean().sort_values(by=["Fall", "Spring"]))

season_columns = list(data.columns)
season_columns.append('Season')

season_data = pandas.DataFrame(columns=season_columns, dtype=float)


print(season_data)


for index, row in data.iterrows():
    for season in season_map[row['Sport']]:
        row['Season'] = season
        season_data.loc[len(season_data)] = list(row)

print(season_data[["Season", "Fall", "Spring"]])

print(1 - season_data[["Season", "Fall", "Spring"]].groupby(
    "Season").mean().sort_values(by=["Fall", "Spring"]))
