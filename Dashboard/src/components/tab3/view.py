import dash_html_components as html
import dash_core_components as dcc
import dash_table as dt
from src.components.datahr import df

def renderIsiTab3() :
    return[
            html.Div([
                html.Div([
                    html.P('Indicators : '),
                    dcc.Dropdown(
                        id='xplothist',
                        options=[i for i in [{'label':'Gender', 'value':'Gender'},
                                            {'label': 'Marital Status', 'value': 'MaritalStatus'},
                                            {'label': 'Work Life Balance', 'value': 'WorkLifeBalance'},
                                            {'label': 'Environment Satisfaction', 'value': 'EnvironmentSatisfaction'},
                                            {'label': 'Job Satisfaction', 'value': 'JobSatisfaction'},
                                            {'label': 'Num Companies Worked', 'value': 'NumCompaniesWorked'},
                                            {'label': 'Job Involvement', 'value': 'JobInvolvement'},
                                            {'label': 'Business Travel', 'value': 'BusinessTravel'},
                                            {'label': 'Department', 'value': 'Department'}]],
                        value='Gender',
                    )
                ], className='col-3'),
            ], className='row'),
            html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),
            dcc.Graph(
                id='histgraph'
            )
        ]   