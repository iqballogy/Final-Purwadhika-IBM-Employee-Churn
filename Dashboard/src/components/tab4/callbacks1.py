import base64
import datetime
import io
import pandas as pd
import dash_table

import pickle
import requests
import dash_html_components as html
loadModel = pickle.load(open('gbc.sav', 'rb'))
le_gender = pickle.load(open('le_Gender.sav', 'rb'))
le_overtime = pickle.load(open('le_OverTime.sav', 'rb'))
le_over18 = pickle.load(open('le_Over18.sav', 'rb'))
le_travel = pickle.load(open('le_BusinessTravel.sav', 'rb'))
le_dept = pickle.load(open('le_Department.sav', 'rb'))
le_edu = pickle.load(open('le_EducationField.sav', 'rb'))
le_job = pickle.load(open('le_JobRole.sav', 'rb'))
le_Marital = pickle.load(open('le_Marital.sav', 'rb'))
minmaxScaler = pickle.load(open('scaler.sav', 'rb'))

    
def callbackpredict(n_clicks,Age,Travel,DRate,Dept,Distance,Education,EducationF,Employee,Number,Env,
                    Gender,Hrate,Involvement,Joblevel,Role,Satis,Marital,Mincome,Mrate,Nc,Over18, Overtime,
                    salaryHike,pp,relationship,Stdh,Stock,TotalWorkingYear,Numtraining,Wlb,Yearat,Yearcr,Ys,yearsec) :

    if(Age != '' and Travel != '' and DRate != '' and Dept != '' and Distance != '' and Education != '' and EducationF != '' and Employee != '' and Number != '' and Env != ''
    and Gender != '' and Hrate != '' and Involvement != '' and Joblevel != '' and Role != '' and Satis != '' and Marital != '' and Mincome != ''
    and Mrate != '' and Nc != '' and Over18 != ''  and Overtime != '' and salaryHike != ''  and pp != '' and relationship != ''
    and Stdh != '' and Stock != '' and TotalWorkingYear != '' and Numtraining != '' and Wlb != '' and Yearat != '' and Yearcr != '' and Ys != '' and yearsec != ''): 
        OverTimeencode = le_overtime.fit_transform([Overtime])
        over18encode = le_over18.fit_transform([Over18])
        travelencode = le_travel.fit_transform([Travel])
        deptencode = le_dept.fit_transform([Dept])
        eduencode = le_edu.fit_transform([EducationF])
        jobencode = le_job.fit_transform([Role])
        maritalencode = le_Marital.fit_transform([Marital])
        Genderencode = le_gender.fit_transform([Gender])

        predictProba = loadModel.predict_proba([[int(Age),travelencode,int(DRate),deptencode,int(Distance),int(Education),eduencode,int(Employee),int(Number),int(Env),
                    Genderencode,int(Hrate),int(Involvement),int(Joblevel),jobencode,int(Satis),maritalencode,int(Mincome),int(Mrate),int(Nc),over18encode, OverTimeencode,
                    int(salaryHike),int(pp),int(relationship),int(Stdh),int(Stock),int(TotalWorkingYear),int(Numtraining),int(Wlb),int(Yearat),int(Yearcr),int(Ys),int(yearsec)]])

        prediction = 'Remain IBM Employee'
        predictSave = 0
        if(predictProba[0,1] > 0.15) :
            prediction = 'Leave IBM'

        return [
            html.H3('Probability of Employee to Quit is : {}%'.format(predictProba[0,1] * 100)),
            html.H3('so we predict the employee will {}'.format(prediction))
        ]
    else :
        return html.H3('Please fill all inputs in the form above to Predict The Employee')