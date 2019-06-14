import base64
import datetime
import io
import pandas as pd
import dash_table
import numpy as np
import pickle
import requests
import dash_html_components as html
from sklearn.preprocessing import MinMaxScaler
from src.components.datahr import df
from sklearn.preprocessing import LabelEncoder

loadModel = pickle.load(open('log.sav', 'rb'))

df = df.drop(['Attrition', 'EmployeeCount', 'EmployeeNumber','StandardHours', 'Over18'], axis=1)

def callbackpredict(n_clicks,Age,Travel,DRate,Dept,Distance,Education,EducationF,Employee,Number,Env,
                    Gender,Hrate,Involvement,Joblevel,Role,Satis,Marital,Mincome,Mrate,Nc,Over18, Overtime,
                    salaryHike,pp,relationship,Stdh,Stock,TotalWorkingYear,Numtraining,Wlb,Yearat,Yearcr,Ys,yearsec) :
    model = df
    if(Age != '' and Travel != '' and DRate != '' and Dept != '' and Distance != '' and Education != '' and EducationF != '' and Employee != '' and Number != '' and Env != ''
    and Gender != '' and Hrate != '' and Involvement != '' and Joblevel != '' and Role != '' and Satis != '' and Marital != '' and Mincome != ''
    and Mrate != '' and Nc != '' and Over18 != ''  and Overtime != '' and salaryHike != ''  and pp != '' and relationship != ''
    and Stdh != '' and Stock != '' and TotalWorkingYear != '' and Numtraining != '' and Wlb != '' and Yearat != '' and Yearcr != '' and Ys != '' and yearsec != ''):

        data = pd.DataFrame([Age,Travel,DRate,Dept,Distance,Education,EducationF,Env,
                Gender,Hrate,Involvement,Joblevel,Role,Satis,Marital,Mincome,Mrate,Nc, Overtime,
                salaryHike,pp,relationship,Stock,TotalWorkingYear,Numtraining,Wlb,Yearat,Yearcr,Ys,yearsec])
        data = data.transpose()
        data.columns = list(model.columns)
        # print(data)
        model = pd.concat([model,data], ignore_index = True, axis = 0)
        print(model)

        #Label Encoder
        encode = LabelEncoder()
        model['Gender'] = encode.fit_transform(model['Gender'])
        model['OverTime'] = encode.fit_transform(model['OverTime'])
        model['PerformanceRating'] = encode.fit_transform(model['PerformanceRating'])

        # One Hot Encoder
        one = ['BusinessTravel', 'Department', 'EducationField','JobRole', 'MaritalStatus']
        model = pd.get_dummies(model, drop_first=True, columns = one)
        print(model.shape)

        
        #Scaler
        scaler = MinMaxScaler(feature_range=(0, 5))
        for col in model.select_dtypes('number'):
            model[col] = model[col].astype(float)
            model[[col]] = scaler.fit_transform(model[[col]])

        predictProba = loadModel.predict_proba([np.array(model.iloc[-1,:])])
        prediction = 'remain an IBM employee'
        if(predictProba[0,1] > 0.15) :
            prediction = 'Leave IBM'
            print(prediction)
        return [
            html.H3('Probability of Employee to Quit is : {}%'.format(predictProba[0,1] * 100)),
            html.H3('so we predict the employee will {}'.format(prediction))
        ]
    else :
        return html.H3('Please fill all inputs in the form above to Predict The Employee')