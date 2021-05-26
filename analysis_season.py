import pandas
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import copy

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
    1: "First-year",
    2: "Sophomore",
    3: "Junior",
    42: 'Red-shirt'
}

season_columns = list(data.columns)
season_columns.append('Season')

rows = []

for index, row in data.iterrows():
    for season in season_map[row['Sport']]:

        copyrow = copy.deepcopy(row)

        if row['Sport'] == 'baseball':
            print(season_map[row['Sport']])

        copyrow['Season'] = season
        rows.append(copyrow)

season_data = pandas.DataFrame(rows, columns=season_columns, dtype=float)


print(season_data)

season_data['Sport'] = data.apply(
    lambda row: row.Sport.replace("-", " ").title().replace("mens", "men's").replace("Mens", "Men's"), axis=1)


fallCount = season_data[["Sport", "Season", "Fall"]
                        ].groupby(["Sport", "Season"]).sum().reset_index()

fallPercent = season_data[["Sport", "Season", "Fall"]
                          ].groupby(["Sport", "Season"]).mean().reset_index()

springCount = season_data[["Sport", "Season", "Spring"]
                          ].groupby(["Sport", "Season"]).sum().reset_index()
springPercent = season_data[["Sport", "Season", "Spring"]
                            ].groupby(["Sport", "Season"]).mean().reset_index()


df = fallCount
df["Student Athletes"] = "Student Athletes"
df["fallCount"] = df["Fall"]
df["fallPercent"] = fallPercent["Fall"]
df["springCount"] = springCount["Spring"]
df["springPercent"] = springPercent["Spring"]

filteredFall = df.loc[df['fallCount'] != 0]
average_gapped_fall = filteredFall['fallPercent'].mean()

filteredSpring = df.loc[df['springCount'] != 0]
average_gapped_spring = filteredSpring['springPercent'].mean()


print(filteredFall)

fallTrace = px.treemap(filteredFall,
                       path=['Student Athletes',
                             'Season', 'Sport'],
                       values='fallCount',
                       color='fallPercent',
                       color_continuous_midpoint=average_gapped_fall,
                       custom_data=['fallCount', 'fallPercent'],
                       ).update_layout(coloraxis=dict(cmid=average_gapped_fall, colorbar=dict(tickformat='%', title=dict(text='Percent on leave')), colorscale='RdBu')).update_traces(visible=True, hovertemplate='%{label}<br>%{customdata[0]} athletes on leave - %{customdata[1]:.2%}').data[0]

springTrace = px.treemap(filteredSpring,
                         path=['Student Athletes',
                               'Season', 'Sport'],
                         values='springCount',
                         color='springPercent',
                         custom_data=['springCount', 'springPercent'],
                         color_continuous_midpoint=average_gapped_spring).update_layout(coloraxis=dict(cmid=average_gapped_fall, colorbar=dict(tickformat='%', title=dict(text='Percent on leave')), colorscale='RdBu')).update_traces(visible=False, hovertemplate='%{label}<br>%{customdata[0]} athletes on leave - %{customdata[1]:.2%}').data[0]

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
                layout=dict(updatemenus=updatemenus))

fig.update_layout(coloraxis=dict(cmid=0.5, colorbar=dict(tickformat='%',
                                                         title=dict(text='Percent on leave')), colorscale='RdBu_r'))

fig.write_html("by_season.html")

# fig.show()
