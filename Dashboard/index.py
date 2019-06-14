import numpy as np
import pandas as pd
import os
import pickle
import dash
import dash_table as dt
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from plotly import tools
import plotly.graph_objs as go

from src.components.datahr import df
from src.components.tab1.view import renderIsiTab1
from src.components.tab2.view import renderIsiTab2
from src.components.tab3.view import renderIsiTab3
from src.components.tab4.view import renderIsiTab4

from src.components.support import legendDict


from src.components.tab1.callbacks import callbacksortingtable,callbackfiltertable
from src.components.tab2.callbacks import callbackpieplot
from src.components.tab3.callbacks import callbackbarplot
from src.components.tab4.callbacks import callbackpredict


app = dash.Dash(__name__)

server = app.server

app.title = 'IBM HR Dashboard'

app.layout = html.Div([
    html.H1('IBM HR Dashboard'),
    html.H3('''
        Created By : Muhammad Iqbal
    '''
    ),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Data Employee', value='tab-1', children=renderIsiTab1()),
        dcc.Tab(label='Demographics Distribution', value='tab-2', children=renderIsiTab2()),
        dcc.Tab(label=' Possible Cause of Attrition', value='tab-3', children=renderIsiTab3()),
        dcc.Tab(label='Test Predict', value='tab-4', children=renderIsiTab4()),
        
        
    ],style={
        'fontFamily': 'system-ui'
    }, content_style={
        'fontFamily': 'Arial',
        'borderBottom': '1px solid #d6d6d6',
        'borderLeft': '1px solid #d6d6d6',
        'borderRight': '1px solid #d6d6d6',
        'padding': '44px'
    }) 
], style={
    'maxWidth': '1200px',
    'margin': '0 auto'
})


# Callback

@app.callback(
    Output('table-multicol-sorting', "data"),
    [Input('table-multicol-sorting', "pagination_settings"),
     Input('table-multicol-sorting', "sorting_settings")])
def update_sort_paging_table(pagination_settings, sorting_settings):
    return callbacksortingtable(pagination_settings,sorting_settings)

@app.callback(
    Output(component_id='tablediv', component_property='children'),
    [Input('buttonsearch', 'n_clicks'),
    Input('filterrowstable', 'value')],
    [State('filterdep', 'value'),
    State('filterjoblevel', 'value'),
    State('filtergender', 'value'),
    State('filterage', 'value'),
    State('filterWorkingYear', 'value'),
    State('filterAttrition', 'value'),
    State('filtermrate', 'value')]
)
def update_table(n_clicks, maxrows,dept, level, gender, Age, year, tendency, salary):
    return callbackfiltertable(n_clicks, maxrows,dept, level, gender, Age, year, tendency, salary)

@app.callback(
    Output(component_id='piegraph', component_property='figure'),
    [Input(component_id='groupplotpie', component_property='value')]
)
def update_pie_plot(group):
    return callbackpieplot(group)


@app.callback(
    Output(component_id='histgraph', component_property='figure'),
    [Input(component_id='xplothist', component_property='value')]
)

def update_hist_plot(xhist):
    return callbackbarplot(xhist)
    
@app.callback(
    Output('outputpredict', 'children'),
    [Input('buttonpredict', 'n_clicks')],
    [State('predictAge', 'value'), 
    State('predictTravel', 'value'),
    State('predictDRate', 'value'),
    State('predictDep', 'value'),
    State('distancePredict', 'value'),
    State('EducationlPredict', 'value'),
    State('educationFPredict', 'value'),
    State('employeePredict', 'value'),
    State('numberPredict', 'value'),
    State('envPredict', 'value'),
    State('genderPredict', 'value'),
    State('hratePredict', 'value'),
    State('involvementPredict', 'value'),
    State('joblevelPredict', 'value'),
    State('rolePredict', 'value'),
    State('satisPredict', 'value'),
    State('maritalPredict', 'value'),
    State('mincomePredict', 'value'),
    State('mratePredict', 'value'),
    State('ncPredict', 'value'),
    State('18Predict', 'value'),
    State('overtimePredict', 'value'),
    State('salaryHikePredict', 'value'),
    State('ppPredict', 'value'),
    State('relationshipPredict', 'value'),
    State('stdhPredict', 'value'),
    State('stockPredict', 'value'),
    State('totalWorkingYearPredict', 'value'),
    State('numtrainingPredict', 'value'),
    State('wlbPredict', 'value'),
    State('yearatPredict', 'value'),
    State('yearcrPredict', 'value'),
    State('ysPredict', 'value'),
    State('yearsecPredict', 'value')
    ])
def testpredict(n_clicks,Age,Travel,DRate,Dept,Distance,Education,EducationF,Employee,Number,Env,
                    Gender,Hrate,Involvement,Joblevel,Role,Satis,Marital,Mincome,Mrate,Nc,Over18, Overtime,
                    salaryHike,pp,relationship,Stdh,Stock,TotalWorkingYear,Numtraining,Wlb,Yearat,Yearcr,Ys,yearsec):
    return callbackpredict(n_clicks,Age,Travel,DRate,Dept,Distance,Education,EducationF,Employee,Number,Env,
                    Gender,Hrate,Involvement,Joblevel,Role,Satis,Marital,Mincome,Mrate,Nc,Over18, Overtime,
                    salaryHike,pp,relationship,Stdh,Stock,TotalWorkingYear,Numtraining,Wlb,Yearat,Yearcr,Ys,yearsec)



if __name__ == '__main__':
    app.run_server(debug=True)