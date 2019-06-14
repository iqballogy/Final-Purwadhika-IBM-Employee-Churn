from src.components.datahr import df

legendDict = {
    'Attrition': { 'Stay': 'No', 'Quit': 'Yes' },
    'Gender' : {i:i for i in df['Gender'].unique()},
    'MaritalStatus' : {i:i for i in df['MaritalStatus'].unique()},
    'WorkLifeBalance' : { 1: 'Score : 1 (Least)', 
                        2: 'Score : 2', 
                        3: 'Score : 3', 
                        4: 'Score : 4 (Best)'},
    'EnvironmentSatisfaction' : { 1: 'Score : 1 (Least)', 
                        2: 'Score : 2', 
                        3: 'Score : 3', 
                        4: 'Score : 4 (Best)'},
    'JobSatisfaction' : { 1: 'Score : 1 (Least)', 
                        2: 'Score : 2', 
                        3: 'Score : 3', 
                        4: 'Score : 4 (Best)'},
    'JobLevel': {i:i for i in df['JobLevel'].unique()},
    'NumCompaniesWorked' : {i:i for i in df['NumCompaniesWorked'].unique()},
    'JobInvolvement' : {i:i for i in df['JobInvolvement'].unique()},
    'BusinessTravel' : { 'Travel_Rarely': 'Travel Rarely', 
                        'Non-Travel': 'Non-Travel Employee', 
                        'Travel_Frequently': 'Travel Frequently'},
    'Department' : {i:i for i in df['Department'].unique()},
    'Age' : {i:i for i in df['Age'].unique()},
    'JobRole' : {i:i for i in df['JobRole'].unique()},
    'Department' : {i:i for i in df['Department'].unique()},
    'EducationField' : {i:i for i in df['EducationField'].unique()},
    'JobRole' : {i:i for i in df['EducationField'].unique()}

}
