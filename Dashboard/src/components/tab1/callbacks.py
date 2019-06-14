import requests
import pandas as pd

from src.components.tab1.view import generate_table
from src.components.datahr import df, dfhr

def callbacksortingtable(pagination_settings, sorting_settings) :
    # print(sorting_settings)
    if len(sorting_settings):
        dff = df.sort_values(
            [col['column_id'] for col in sorting_settings],
            ascending=[
                col['direction'] == 'asc'
                for col in sorting_settings
            ],
            inplace=False
        )
    else:
        # No sort is applied
        dff = df

    return dff.iloc[
        pagination_settings['current_page']*pagination_settings['page_size']:
        (pagination_settings['current_page'] + 1)*pagination_settings['page_size']
    ].to_dict('rows')

def callbackfiltertable(n_clicks, maxrows,dept, level, gender, Age, year, tendency, salary):
    global df
    df = dfhr
    if(dept != '' and level != '' and gender != '' and 
    Age != '' and year != '' and tendency != '' and salary != ''):
         df = df[(df['Department'] == dept) & 
         (df['JobLevel'] == level) & 
         (df['Gender'] == gender) & 
         (df['Age'] >= min(Age)) &
         (df['Age'] <= max(Age)) &
         (df['TotalWorkingYears'] >= min(year)) &
         (df['TotalWorkingYears'] <= max(year)) &
         (df['Attrition'] == tendency) & 
         (df['MonthlyRate'] >= min(salary))&
         (df['MonthlyRate'] <= max(salary))]
    else:
        df
    
    return generate_table(df, pagesize=maxrows)
