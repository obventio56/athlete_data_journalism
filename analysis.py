import pandas
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

data = pandas.read_csv('athlete_data.csv')

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

gradeMap = {
    1: "Freshman",
    2: "Sophomore",
    3: "Junior",
    42: 'Red-shirt'
}


data['SportGender'] = data.apply(lambda row: sport_gender[row.Sport], axis=1)
data['Grade'] = data.apply(lambda row: gradeMap[row.Grade], axis=1)
data['Sport'] = data.apply(
    lambda row: row.Sport.replace("-", " ").title().replace("mens", "men's").replace("Mens", "Men's"), axis=1)
data['total'] = 1

fallGradeCount = data[["Grade", "Sport", "SportGender", "Fall"]
                      ].groupby(["Grade", "Sport", "SportGender"]).sum().reset_index()
fallGradeTotal = data[["Grade", "Sport", "SportGender", "Fall"]
                      ].groupby(["Grade", "Sport", "SportGender"]).count().reset_index()
fallGradeCount['Total'] = fallGradeTotal['Fall']


springGradeCount = data[["Grade", "Sport", "SportGender", "Spring"]
                        ].groupby(["Grade", "Sport", "SportGender"]).sum().reset_index()
springGradeTotal = data[["Grade", "Sport", "SportGender", "Spring"]
                        ].groupby(["Grade", "Sport", "SportGender"]).count().reset_index()
springGradeCount['Total'] = springGradeTotal['Spring']


fallSportCount = data[["Grade", "Sport", "SportGender", "Fall"]
                      ].groupby(["Sport", "SportGender"]).sum().reset_index()
fallSportTotal = data[["Grade", "Sport", "SportGender", "Fall"]
                      ].groupby(["Sport", "SportGender"]).count().reset_index()
fallSportCount['Total'] = fallSportTotal['Fall']


springSportCount = data[["Grade", "Sport", "SportGender", "Spring"]
                        ].groupby(["Sport", "SportGender"]).sum().reset_index()
springSportTotal = data[["Grade", "Sport", "SportGender", "Spring"]
                        ].groupby(["Sport", "SportGender"]).count().reset_index()
springSportCount['Total'] = springSportTotal['Spring']


fallGenderCount = data[["Grade", "Sport", "SportGender", "Fall"]
                       ].groupby(["SportGender"]).sum().reset_index()
fallGenderTotal = data[["Grade", "Sport", "SportGender", "Fall"]
                       ].groupby(["SportGender"]).count().reset_index()
fallGenderCount['Total'] = fallGenderTotal['Fall']


springGenderCount = data[["Grade", "Sport", "SportGender", "Spring"]
                         ].groupby(["SportGender"]).sum().reset_index()
springGenderTotal = data[["Grade", "Sport", "SportGender", "Spring"]
                         ].groupby(["SportGender"]).count().reset_index()
springGenderCount['Total'] = springGenderTotal['Spring']

fallTotal = data[["Grade", "Sport", "SportGender", "Fall"]].count()
fallCount = data[["Grade", "Sport", "SportGender", "Fall"]].sum()

springTotal = data[["Grade", "Sport", "SportGender", "Spring"]].count()
springCount = data[["Grade", "Sport", "SportGender", "Spring"]].sum()

columns = ["Name", "Parent", "Count", "Total", "Color", "ID"]
root = 'Student Athletes'


dfFall = pandas.DataFrame(columns=columns, dtype=float)
dfFall.loc[len(dfFall.index)] = [root, None,
                                 fallCount['Fall'], fallTotal['Fall'], 0, root]

for index, row in fallGradeCount.iterrows():
    copyrow = [row['Grade'], row['Sport'] + row['SportGender'], row['Fall'], row['Total'],
               0, row['Grade'] + row['Sport'] + row['SportGender']]
    dfFall.loc[len(dfFall.index)] = copyrow
for index, row in fallSportCount.iterrows():
    copyrow = [row['Sport'], row['SportGender'], row['Fall'],
               row['Total'], 0, row['Sport'] + row['SportGender']]
    dfFall.loc[len(dfFall.index)] = copyrow
for index, row in fallGenderCount.iterrows():
    copyrow = [row['SportGender'], root, row['Fall'], row['Total'],
               0, row['SportGender']]
    dfFall.loc[len(dfFall.index)] = copyrow
dfFall["Color"] = dfFall.apply(lambda row: row['Count']/row['Total'], axis=1)

dfFall = dfFall.loc[dfFall['Count'] != 0]


dfSpring = pandas.DataFrame(columns=columns, dtype=float)
dfSpring.loc[len(dfSpring.index)] = [root, None,
                                     springCount['Spring'], springTotal['Spring'], 0, root]

for index, row in springGradeCount.iterrows():
    copyrow = [row['Grade'], row['Sport'] + row['SportGender'], row['Spring'], row['Total'],
               0, row['Grade'] + row['Sport'] + row['SportGender']]
    dfSpring.loc[len(dfSpring.index)] = copyrow
for index, row in springSportCount.iterrows():
    copyrow = [row['Sport'], row['SportGender'],
               row['Spring'], row['Total'], 0, row['Sport'] + row['SportGender']]
    dfSpring.loc[len(dfSpring.index)] = copyrow
for index, row in springGenderCount.iterrows():
    copyrow = [row['SportGender'], root, row['Spring'], row['Total'],
               0, row['SportGender']]
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
                layout_title_text="Student-athletes on leave by gender, sport, and year.",
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

fig.show()

# fig.write_html("by_gender_2.html")
