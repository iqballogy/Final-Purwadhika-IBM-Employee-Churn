import dash_html_components as html
import dash_core_components as dcc
from src.components.datahr import df

def renderIsiTab4() :
    return [
        html.Center([
            html.H3('Attrition Predict',className='title')
        ]),
        html.Div([
            html.Div(id='output-data-upload')
        ], className='row'),
        html.Div([
            html.Div([
                    html.P('Age : '),
                    dcc.Input(
                        id='predictAge',
                        type='number',
                        value=10,
                        style=dict(width='100%')
                    )
            ], className='col-3'),
            html.Div([
                    html.P('Business Travel : '),
                    dcc.Dropdown(
                        id='predictTravel',
                        options=[i for i in [{'label': 'Travel Rarely', 'value': 'Travel_Rarely' },
                                            { 'label': 'Travel Frequently', 'value': 'Travel_Frequently' },
                                            { 'label': 'Non-Travel', 'value': 'Non-Travel' }]],
                        value='Travel_Rarely'
                    )
            ], className='col-3'),
            html.Div([
                    html.P('Daily Rate : '),
                    dcc.Input(
                        id='predictDRate',
                        type='number',
                        value=50,
                        style=dict(width='100%')
                    )
            ], className='col-3'),
            html.Div([
                    html.P('Department : '),
                    dcc.Dropdown(
                        id='predictDep',
                        options= [{'label': i, 'value': i} for i in df['Department'].unique()],
                        value='Sales'
                    )
                ], className='col-3'),
        ], className='row paddingtop'),
        html.Div([
            html.Div([
                    html.P('Home Distace Cat. : '),
                    dcc.Dropdown(
                        id='distancePredict',
                        options= [{'label': i, 'value': i} for i in df['DistanceFromHome'].unique()],
                        value=3
                    )
                ], className='col-3'),
            html.Div([
                    html.P('Education Level Category : '),
                    dcc.Dropdown(
                        id='EducationlPredict',
                        options= [{'label': i, 'value': i} for i in df['Education'].unique()],
                        value=1
                    )
                ], className='col-3'),
            html.Div([
                    html.P('Education Field : '),
                    dcc.Dropdown(
                        id='educationFPredict',
                        options= [{'label': i, 'value': i} for i in df['EducationField'].unique()],
                        value='Other'
                    )
                ], className='col-3'),
            html.Div([
                    html.P('Employee Count. : '),
                    dcc.Dropdown(
                        id='employeePredict',
                        options= [{'label': i, 'value': i} for i in df['EmployeeCount'].unique()],
                        value=1
                    )
                ], className='col-3'),
        ], className='row paddingtop'),
        html.Div([
            html.Div([
                    html.P('Employee Number : '),
                    dcc.Input(
                        id='numberPredict',
                        type='number',
                        value=1498,
                        style=dict(width='100%')
                    )
            ], className='col-3'),
            html.Div([
                    html.P('Environment Satisfaction : '),
                    dcc.Dropdown(
                        id='envPredict',
                        options= [{'label': i, 'value': i} for i in df['EnvironmentSatisfaction'].unique()],
                        value=4
                    )
                ], className='col-3'),
            html.Div([
                    html.P('Gender : '),
                    dcc.Dropdown(
                        id='genderPredict',
                        options= [{'label': i, 'value': i} for i in df['Gender'].unique()],
                        value='Male'
                    )
                ], className='col-3'),
            html.Div([
                    html.P('Hourly rate : '),
                    dcc.Input(
                        id='hratePredict',
                        type='number',
                        value=50,
                        style=dict(width='100%')
                    )
            ], className='col-3'),
        ], className='row paddingtop'),
        html.Div([
            html.Div([
                    html.P('Job Involvement Level : '),
                    dcc.Dropdown(
                        id='involvementPredict',
                        options= [{'label': i, 'value': i} for i in df['JobInvolvement'].unique()],
                        value=3
                    )
                ], className='col-3'),
            html.Div([
                    html.P('Job Level : '),
                    dcc.Dropdown(
                        id='joblevelPredict',
                        options= [{'label': i, 'value': i} for i in df['JobLevel'].unique()],
                        value=4
                    )
                ], className='col-3'),
            html.Div([
                    html.P('Job Role : '),
                    dcc.Dropdown(
                        id='rolePredict',
                        options= [{'label': i, 'value': i} for i in df['JobRole'].unique()],
                        value='Manager'
                    )
                ], className='col-3'),
            html.Div([
                    html.P('Job Satisfaction : '),
                    dcc.Dropdown(
                        id='satisPredict',
                        options= [{'label': i, 'value': i} for i in df['JobSatisfaction'].unique()],
                        value=1
                    )
                ], className='col-3'),
        ], className='row paddingtop'),
        html.Div([
            html.Div([
                    html.P('Marital Status : '),
                    dcc.Dropdown(
                        id='maritalPredict',
                        options= [{'label': i, 'value': i} for i in df['MaritalStatus'].unique()],
                        value='Single'
                    )
                ], className='col-3'),
            html.Div([
                    html.P('Monthly Income : '),
                    dcc.Input(
                        id='mincomePredict',
                        type='number',
                        value=50,
                        style=dict(width='100%')
                    )
            ], className='col-3'),
            html.Div([
                    html.P('Monthly Rate : '),
                    dcc.Input(
                        id='mratePredict',
                        type='number',
                        value=50,
                        style=dict(width='100%')
                    )
            ], className='col-3'),
            html.Div([
                    html.P('Num Companies Worked: '),
                    dcc.Input(
                        id='ncPredict',
                        type='number',
                        value=7,
                        style=dict(width='100%')
                    )
            ], className='col-3'),
        ], className='row paddingtop'),
        html.Div([
            html.Div([
                    html.P('Over 18 : '),
                    dcc.Dropdown(
                        id='18Predict',
                        options= [{'label': i, 'value': i} for i in df['Over18'].unique()],
                        value='Y'
                    )
                ], className='col-3'),
            html.Div([
                    html.P('Overtime : '),
                    dcc.Dropdown(
                        id='overtimePredict',
                        options= [{'label': i, 'value': i} for i in df['OverTime'].unique()],
                        value='Yes'
                    )
                ], className='col-3'),
            html.Div([
                    html.P('Pct. Salary Hike : '),
                    dcc.Input(
                        id='salaryHikePredict',
                        type='number',
                        value=11,
                        style=dict(width='100%')
                    )
            ], className='col-3'),
            html.Div([
                    html.P('Performance Rating : '),
                    dcc.Dropdown(
                        id='ppPredict',
                        options= [{'label': i, 'value': i} for i in df['PerformanceRating'].unique()],
                        value=3
                    )
                ], className='col-3'),
        ], className='row paddingtop'),
        html.Div([
            html.Div([
                    html.P('Relationship Satisfaction : '),
                    dcc.Dropdown(
                        id='relationshipPredict',
                        options= [{'label': i, 'value': i} for i in df['RelationshipSatisfaction'].unique()],
                        value=1
                    )
                ], className='col-3'),
            html.Div([
                    html.P('Standard Hours : '),
                    dcc.Dropdown(
                        id='stdhPredict',
                        options= [{'label': i, 'value': i} for i in df['StandardHours'].unique()],
                        value=80
                    )
                ], className='col-3'),
            html.Div([
                    html.P('Stock Option Level : '),
                    dcc.Dropdown(
                        id='stockPredict',
                        options= [{'label': i, 'value': i} for i in df['StockOptionLevel'].unique()],
                        value=0
                    )
                ], className='col-3'),
            html.Div([
                    html.P('Total Working Years : '),
                    dcc.Input(
                        id='totalWorkingYearPredict',
                        type='number',
                        value=8,
                        style=dict(width='100%')
                    )
            ], className='col-3'),
        ], className='row paddingtop'),
        html.Div([
            html.Div([
                    html.P('Number of Training : '),
                    dcc.Input(
                        id='numtrainingPredict',
                        type='number',
                        value=3,
                        style=dict(width='100%')
                    )
            ], className='col-3'),
            html.Div([
                    html.P('WorkLife Balance Score: '),
                    dcc.Dropdown(
                        id='wlbPredict',
                        options= [{'label': i, 'value': i} for i in df['WorkLifeBalance'].unique()],
                        value=1
                    )
                ], className='col-3'),
            html.Div([
                    html.P('Years at Company : '),
                    dcc.Input(
                        id='yearatPredict',
                        type='number',
                        value=3,
                        style=dict(width='100%')
                    )
            ], className='col-3'),
            html.Div([
                    html.P('Years InCurrent Role : '),
                    dcc.Input(
                        id='yearcrPredict',
                        type='number',
                        value=8,
                        style=dict(width='100%')
                    )
            ], className='col-3'),
        ], className='row paddingtop'),
        html.Div([
            html.Div([
                    html.P('Years Since Last Promotion : '),
                    dcc.Input(
                        id='ysPredict',
                        type='number',
                        value=3,
                        style=dict(width='100%')
                    )
            ], className='col-3'),
            html.Div([
                    html.P('Years With Current Manager: '),
                    dcc.Dropdown(
                        id='yearsecPredict',
                        options= [{'label': i, 'value': i} for i in df['WorkLifeBalance'].unique()],
                        value=2
                    )
                ], className='col-3'),
            html.Div([
                html.Button('Predict', id='buttonpredict', style=dict(width='100%',marginTop='32px'))
            ], className='col-3')
        ], className='row paddingtop'),
        html.Div([
        html.Center([
    
        ], id='outputpredict', className='paddingtop')])
    ]