import requests
import pandas as pd
import plotly.graph_objs as go
from src.components.tab1.view import generate_table
from src.components.support import legendDict
from src.components.datahr import df, dfhr

def callbackbarplot(xhist):
    groupedTrue  = df[df['Attrition'] == 'Yes'][xhist].value_counts()
    groupedFalse = df[df['Attrition'] == 'No'][xhist].value_counts()
    return dict(
        data=[
            go.Bar(x=groupedTrue.index, 
                    y=groupedTrue.values,
                    name='Quit',
                    marker=dict(
                    color='rgb(49,130,189)'
                        )
                    ),
            go.Bar(x=groupedFalse.index, 
                    y=groupedFalse.values, 
                    name='Stay',
                    marker=dict(
                    color='rgb(204,204,204)'
                        )
                    )
            ],
        layout=go.Layout(
                   title="Attrition Distribution Based on {}".format(xhist),
                    xaxis=dict(title='Value'),
                    yaxis=dict(title='Count'),
                    bargap=0.2,
                    bargroupgap=0.1
                )
    )