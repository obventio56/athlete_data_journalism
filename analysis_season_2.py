import pandas
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import copy

rawData = pandas.read_csv('athlete_data.csv')

sport_gender = {"mens-basketball": "Men's Sport",
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

gradeMap = {
    1: "Freshman",
    2: "Sophomore",
    3: "Junior",
    42: 'Red-shirt'
}

season_columns = list(rawData.columns)
season_columns.append('Season')
rows = []

for index, row in rawData.iterrows():
    for season in season_map[row['Sport']]:
        copyrow = copy.deepcopy(row)
        copyrow['Season'] = season
        rows.append(copyrow)

data = pandas.DataFrame(rows, columns=season_columns, dtype=float)
data['Sport'] = data.apply(
    lambda row: row.Sport.replace("-", " ").title().replace("mens", "men's").replace("Mens", "Men's"), axis=1)

fallSportCount = data[["Grade", "Sport", "Season", "Fall"]
                      ].groupby(["Sport", "Season"]).sum().reset_index()
fallSportTotal = data[["Grade", "Sport", "Season", "Fall"]
                      ].groupby(["Sport", "Season"]).count().reset_index()
fallSportCount['Total'] = fallSportTotal['Fall']


springSportCount = data[["Grade", "Sport", "Season", "Spring"]
                        ].groupby(["Sport", "Season"]).sum().reset_index()
springSportTotal = data[["Grade", "Sport", "Season", "Spring"]
                        ].groupby(["Sport", "Season"]).count().reset_index()
springSportCount['Total'] = springSportTotal['Spring']


fallSeasonCount = data[["Grade", "Sport", "Season", "Fall"]
                       ].groupby(["Season"]).sum().reset_index()
fallSeasonTotal = data[["Grade", "Sport", "Season", "Fall"]
                       ].groupby(["Season"]).count().reset_index()
fallSeasonCount['Total'] = fallSeasonTotal['Fall']


springSeasonCount = data[["Grade", "Sport", "Season", "Spring"]
                         ].groupby(["Season"]).sum().reset_index()
springSeasonTotal = data[["Grade", "Sport", "Season", "Spring"]
                         ].groupby(["Season"]).count().reset_index()
springSeasonCount['Total'] = springSeasonTotal['Spring']

fallTotal = data[["Grade", "Sport", "Season", "Fall"]].count()
fallCount = data[["Grade", "Sport", "Season", "Fall"]].sum()

springTotal = data[["Grade", "Sport", "Season", "Spring"]].count()
springCount = data[["Grade", "Sport", "Season", "Spring"]].sum()

columns = ["Name", "Parent", "Count", "Total", "Color", "ID"]
root = 'Student Athletes'


dfFall = pandas.DataFrame(columns=columns, dtype=float)
dfFall.loc[len(dfFall.index)] = [root, None,
                                 fallCount['Fall'], fallTotal['Fall'], 0, root]

for index, row in fallSportCount.iterrows():
    copyrow = [row['Sport'], row['Season'], row['Fall'],
               row['Total'], 0, row['Sport'] + row['Season']]
    dfFall.loc[len(dfFall.index)] = copyrow
for index, row in fallSeasonCount.iterrows():
    copyrow = [row['Season'], root, row['Fall'],
               row['Total'], 0, row['Season']]
    dfFall.loc[len(dfFall.index)] = copyrow
dfFall["Color"] = dfFall.apply(lambda row: row['Count']/row['Total'], axis=1)

dfFall = dfFall.loc[dfFall['Count'] != 0]

dfSpring = pandas.DataFrame(columns=columns, dtype=float)
dfSpring.loc[len(dfSpring.index)] = [root, None,
                                     springCount['Spring'], springTotal['Spring'], 0, root]


for index, row in springSportCount.iterrows():
    copyrow = [row['Sport'], row['Season'],
               row['Spring'], row['Total'], 0, row['Sport'] + row['Season']]
    dfSpring.loc[len(dfSpring.index)] = copyrow
for index, row in springSeasonCount.iterrows():
    copyrow = [row['Season'], root, row['Spring'],
               row['Total'], 0, row['Season']]
    dfSpring.loc[len(dfSpring.index)] = copyrow
dfSpring["Color"] = dfSpring.apply(
    lambda row: row['Count']/row['Total'], axis=1)

dfSpring = dfSpring.loc[dfSpring['Count'] != 0]

fallTrace = px.treemap(
    dfFall,
    names='Name',
    parents='Parent',
    ids='ID',
    values='Count',
    color='Color',
    custom_data=['Count', 'Total', 'Color', 'Name'],
).update_layout(
    coloraxis=dict(
        colorbar=dict(tickformat='%', title=dict(text='Percent on leave')
                      ),
        colorscale='RdBu'
    )
).update_traces(
    branchvalues='total',
    visible=True,
    hovertemplate='%{customdata[3]}<br>%{customdata[0]}/%{customdata[1]} athletes on leave - %{customdata[2]:.2%}'
).data[0]

springTrace = px.treemap(
    dfSpring,
    names='Name',
    parents='Parent',
    ids='ID',
    values='Count',
    color='Color',
    custom_data=['Count', 'Total', 'Color', 'Name'],
).update_layout(
    coloraxis=dict(
        colorbar=dict(tickformat='%', title=dict(text='Percent on leave')
                      ),
        colorscale='RdBu'
    )
).update_traces(
    branchvalues='total',
    visible=False,
    hovertemplate='%{customdata[3]}<br>%{customdata[0]}/%{customdata[1]} athletes on leave - %{customdata[2]:.2%}'
).data[0]

updatemenus = [{'active': 0, "buttons": [
    dict(label="Fall",
         method="update",
         args=[{"visible": [True, False]},

               ]),
    dict(label="Spring",
         method="update",
         args=[{"visible": [False, True]},
               ])
]}]

fig = go.Figure(data=[fallTrace, springTrace],
                layout_title_text="Student-athletes on leave by season and sport.",
                layout_annotations=[dict(
                    x=-0.072,
                    y=1.073,
                    showarrow=False,
                    xref="paper", yref="paper",
                    text='This graph is interactive. Hover to see exact figures or click to expand a specific box.')],
                layout=dict(updatemenus=updatemenus)
                )

fig.update_layout(coloraxis=dict(cmid=0.5, colorbar=dict(tickformat='%',
                                                         title=dict(text='Percent on leave')), colorscale='RdBu_r'))

# fig.show()

fig.write_html("by_season_3.html")
