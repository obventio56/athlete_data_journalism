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
    1: "First-year",
    2: "Sophomore",
    3: "Junior",
    42: 'Red-shirt'
}


data['SportGender'] = data.apply(lambda row: sport_gender[row.Sport], axis=1)
data['Grade'] = data.apply(lambda row: gradeMap[row.Grade], axis=1)
data['Sport'] = data.apply(
    lambda row: row.Sport.replace("-", " ").title(), axis=1)
data['total'] = 1

print(data)


fallCount = data[["Grade", "Sport", "SportGender", "Fall"]
                 ].groupby(["Grade", "Sport", "SportGender"]).sum().reset_index()
fallPercent = data[["Grade", "Sport", "SportGender", "Fall"]
                   ].groupby(["Grade", "Sport", "SportGender"]).mean().reset_index()
springCount = data[["Grade", "Sport", "SportGender", "Spring"]
                   ].groupby(["Grade", "Sport", "SportGender"]).sum().reset_index()
springPercent = data[["Grade", "Sport", "SportGender", "Spring"]
                     ].groupby(["Grade", "Sport", "SportGender"]).mean().reset_index()
total = data[["Grade", "Sport", "SportGender", "total"]
             ].groupby(["Grade", "Sport", "SportGender"]).sum().reset_index()


df = fallCount
df["Student Athletes"] = "Student Athletes"
df["fallCount"] = df["Fall"]
df["fallPercent"] = fallPercent["Fall"]
df["springCount"] = springCount["Spring"]
df["springPercent"] = springPercent["Spring"]
df['Total'] = total['total']

filteredFall = df.loc[df['fallCount'] != 0]
average_gapped_fall = filteredFall['fallPercent'].mean()

filteredSpring = df.loc[df['springCount'] != 0]
average_gapped_spring = filteredSpring['springPercent'].mean()


fallTrace = px.treemap(filteredFall,
                       path=['Student Athletes',
                             'SportGender', 'Sport', 'Grade'],
                       values='fallCount',
                       color='fallPercent',
                       color_continuous_midpoint=average_gapped_fall,
                       custom_data=['fallCount', 'fallPercent', 'Total'],
                       ).update_layout(coloraxis=dict(cmid=average_gapped_fall, colorbar=dict(tickformat='%', title=dict(text='Percent on leave')), colorscale='RdBu')).update_traces(visible=True, hovertemplate='%{customdata[0]} athletes on leave - %{customdata[1]:.2%}').data[0]

springTrace = px.treemap(filteredSpring,
                         path=['Student Athletes',
                               'SportGender', 'Sport', 'Grade'],
                         values='springCount',
                         color='springPercent',
                         custom_data=['springCount', 'springPercent', 'Total'],
                         color_continuous_midpoint=average_gapped_spring).update_layout(coloraxis=dict(cmid=average_gapped_fall, colorbar=dict(tickformat='%', title=dict(text='Percent on leave')), colorscale='RdBu')).update_traces(visible=False, hovertemplate='%{customdata[0]} athletes on leave - %{customdata[1]:.2%}').data[0]

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
                layout=dict(updatemenus=updatemenus))

fig.update_layout(coloraxis=dict(cmid=0.5, colorbar=dict(tickformat='%',
                                                         title=dict(text='Percent on leave')), colorscale='RdBu_r'))

fig.show()


"""
print(data[["Sport", "Fall", "Spring"]].groupby(
    "Sport").mean().sort_values(by=["Fall", "Spring"]))
print(data[["Grade", "Fall", "Spring"]].groupby(
    "Grade").mean().sort_values(by=["Fall", "Spring"]))
print(data[["Gender", "Fall", "Spring"]].groupby(
    "Gender").mean().sort_values(by=["Fall", "Spring"]))

"""
