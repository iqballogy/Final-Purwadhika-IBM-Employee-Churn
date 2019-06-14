import dash_html_components as html
import dash_core_components as dcc
import dash_table as dt
from src.components.datahr import df

def renderIsiTab2() :
    return[
             html.Div([
                html.Div([
                    html.P('Indicator: '),
                    dcc.Dropdown(
                        id='groupplotpie',
                        options= [i for i in [{'label': 'Age', 'value': 'Age'},
                                            {'label':'Gender', 'value':'Gender'},
                                            {'label': 'Marital Status', 'value': 'MaritalStatus'},
                                            {'label': 'Department', 'value': 'Department'},
                                            {'label': 'Education Field', 'value': 'EducationField'},
                                            {'label': 'Num Companies Worked', 'value': 'NumCompaniesWorked'},
                                            {'label': 'Job Level', 'value': 'JobLevel'},
                                            {'label': 'Business Travel', 'value': 'BusinessTravel'}]],
                            value='Gender',
                    )
                    ], className='col-4')
                ], className='row'),
                html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),
                dcc.Graph(
                id='piegraph'
                )
        ]   