import dash_html_components as html
import dash_core_components as dcc
import dash_table as dt
from src.components.datahr import df


# def generate_table(dataframe, max_rows=10) :
#     return html.Table(
#          # Header
#         [html.Tr([html.Th(col) for col in dataframe.columns])] +

#         # Body
#         [html.Tr([
#             html.Td(str(dataframe.iloc[i,col])) for col in range(len(dataframe.columns))
#         ]) for i in range(min(len(dataframe), max_rows))]
#     )
def generate_table(dataframe, pagesize=10):
    return dt.DataTable(
                id='table-multicol-sorting',
                columns=[
                    {"name": i, "id": i} for i in dataframe.columns
                ],
                data=df.to_dict('rows'),
                style_table={'overflowX': 'scroll'},
                pagination_settings={
                    'current_page': 0,
                    'page_size': pagesize
                },
                pagination_mode='be',
                sorting='be',
                sorting_type='multi',
                sorting_settings=[]
            )

def renderIsiTab1() :
    return [
            html.Div([
                html.Div([
                    html.P('Department : '),
                    dcc.Dropdown(
                        id='filterdep',
                        options= [{'label': i, 'value': i} for i in df['Department'].unique()],
                        value=''
                    )
                ], className='col-4'),
                html.Div([
                    html.P('Level : '),
                    dcc.Dropdown(
                        id='filterjoblevel',
                        options=[{'label': i, 'value': i} for i in range(1,6)],
                        value= 1
                    )
                ], className='col-4'),
                html.Div([
                    html.P('Gender : '),
                    dcc.Dropdown(
                        id='filtergender',
                        options=[{'label': i, 'value': i} for i in df['Gender'].unique()],
                        value='Male'
                    )
                ], className='col-4')
            ], className='row'),
            html.Br(),
            html.Div([
                html.Div([
                    html.P('Range of Age : '),
                    dcc.RangeSlider(
                        marks={i: str(i) for i in range(df['Age'].min(), df['Age'].max()+1,5)},
                        min=df['Age'].min(),
                        max=df['Age'].max(),
                        value=[df['Age'].min(),df['Age'].max()],
                        className='rangeslider',
                        id='filterage'
                    )
                ], className='col-4'),
                html.Div([
                    html.P('Total Working Year : '),
                    dcc.RangeSlider(
                        marks={i: str(i) for i in range(df['TotalWorkingYears'].min(), df['TotalWorkingYears'].max()+1,5)},
                        min=df['TotalWorkingYears'].min(),
                        max=df['TotalWorkingYears'].max(),
                        value=[df['TotalWorkingYears'].min(),df['TotalWorkingYears'].max()],
                        className='rangeslider',
                        id='filterWorkingYear'
                    )
                ], className='col-4'),
                html.Div([
                    html.P('Attrition Tendency : '),
                    dcc.Dropdown(
                        id='filterAttrition',
                        options=[i for i in [{'label': 'All', 'value': '' },
                                            { 'label': 'Stay', 'value': 'No' },
                                            { 'label': 'Quit', 'value': 'Yes' }]],
                        value= ''
                    )
                ], className='col-4'),
            ], className='row'),
            html.Br(),
            html.Div([
                html.Div([
                    html.P('Range of Salary : '),
                    dcc.RangeSlider(
                        marks={i:i for i in range(2000,24501,2500)},
                        min=2000,
                        max=25000,
                        value=[2000,25000],
                        className='rangeslider',
                        id='filtermrate'
                    )
                ], className='col-10'),
                html.Div([
                    html.Br(),
                    html.Button('Search', id='buttonsearch', style=dict(width='100%'))
                ], className='col-2'),
                html.Div([
                ],className='col-1'),
            ], className='row'),
            html.Br(),
            html.Div([
                html.Div([
                    html.P('Maximum Rows : '),
                    dcc.Input(
                        id='filterrowstable',
                        type='number',
                        value=10,
                        style=dict(width='100%')
                    )
                ], className='col-1')
            ], className='row'),
            html.Center([
                html.H2('Employee Data', className='title'),
                html.Div(id='tablediv', children=generate_table(df))
            ])
        ]