import requests
import pandas as pd
import plotly.graph_objs as go
from src.components.tab1.view import generate_table
from src.components.support import legendDict
from src.components.datahr import df, dfhr

def callbackpieplot(group):
    return dict(
                data=[
                    go.Pie(
                        labels=[legendDict[group][val] for val in df[group].unique()],
                        values=[
                            len(df[df[group] == val])
                            for val in df[group].unique()
                        ]
                    )
                ],
                layout=go.Layout(
                    title='Demographics Pie Chart',
                    margin={'l': 160, 'b': 40, 't': 40, 'r': 10}
                )
            )
