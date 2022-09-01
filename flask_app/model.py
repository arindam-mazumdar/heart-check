import pandas as pd
import numpy as np
import pickle


from sklearn.naive_bayes import MultinomialNB


path = '/home/arindam/codes/BRFS/LLCP2020ASC/'
df = pd.read_csv(path+'wrangled_data.csv')
df = df.drop('Unnamed: 0', axis=1)
#df['BMI'] = df['WTKG3']/(pow(df['HEIGHT']/100., 2))
df=df[df['_AGEG5YR']!=14]

age_list = ['18 to 24','25 to 29','30 to 34','35 to 39','40 to 44','45 to 49','50 to 54','55 to 59','60 to 64','65 to 69','70 to 74','75 to 79','80 or older']
sex_list = ['Male','Female']
smoke_list = ['Current smoker - now smokes every day','Current smoker - now smokes some days','Former smoker','Never smoked']
todo_list = ['Had physical activity or exercise in last 30 days', 'No physical activity or exercise in last 30 days']
hcov_list = ['Had health care coverage always', 'Did not have health care coverage always']
sleep_list = ['3','4','5','6','7','8','9','10','11']
drink_list = ['No', 'Yes']
diab_list = ['No', 'Yes']

df=df[['_SEX','_AGEG5YR','_HCVU651','DIABETE4','_TOTINDA','_RFDRHV7','SLEPTIM1','SMOKE','MICHD']].astype(int)
X = np.array(df[['_SEX','_AGEG5YR','_HCVU651','DIABETE4','_TOTINDA','_RFDRHV7','SLEPTIM1','SMOKE']])
y = np.array(df['MICHD'])
clf = MultinomialNB()
clf.fit(X, y)


pickle.dump(clf, open('NB_fitted', 'wb'))


def calculate_factor(age,sex,smoke, todo, hcov,sleep, drink,diab):
    for i in range(len(age_list)):
       if age == age_list[i]:
            age_num = i+1
    for i in range(len(sex_list)):
        if sex == sex_list[i]:
            sex_num = i+1
    for i in range(len(smoke_list)):
        if smoke == smoke_list[i]:
            smoke_num = i+1
    for i in range(len(todo_list)):
        if todo == todo_list[i]:
            todo_num = i+1
    for i in range(len(hcov_list)):
        if hcov == hcov_list[i]:
            hcov_num = i+1
    sleep_num = int(sleep)
    for i in range(len(drink_list)):
        if drink == drink_list[i]:
            drink_num = i+1
    for i in range(len(diab_list)):
        if diab == diab_list[i]:
            diab_num = i
    
    df1 = df[(df['_AGEG5YR']== age_num)]
    df2 = df[(df['SMOKE'] == smoke_num)] 
    df3 = df[(df['_SEX'] == sex_num)]
    df4 = df[(df['_TOTINDA']== todo_num)]
    df5 = df[(df['_HCVU651']== hcov_num)] 
    df6 = df[(df['SLEPTIM1']== sleep_num)] 
    df7 = df[(df['_RFDRHV7']== drink_num)]
    df8 = df[(df['DIABETE4']== diab_num)]
    df_list = [df3,df4,df5,df6,df7,df8]
    prob_list = [(sum(newdf['MICHD'])/len(newdf['MICHD']))*100. for newdf in df_list]
    case_list = ['Smoking', 'Lack of Physical Ativity', 'Lack of Health Coverage', 'Less Sleeping', 'Drinking','History of Diabetis']
    for i in range(len(prob_list)):    
        if max(prob_list) == prob_list[i]:
            return case_list[i]
            
            
            
factor_list = []
fac_dict = dict()
for i, age in enumerate(age_list):
    age_num = i+1
    newdf = df[(df['_AGEG5YR']== age_num)]
    factor_list.append((sum(newdf['MICHD'])/len(newdf['MICHD']))*100.)
fac_dict['age'] = dict(zip(age_list,factor_list))
factor_list = []    
for i, sex in enumerate(sex_list):
    sex_num = i+1
    newdf = df[(df['_SEX'] == sex_num)]
    factor_list.append((sum(newdf['MICHD'])/len(newdf['MICHD']))*100.)
fac_dict['sex'] = dict(zip(sex_list,factor_list))
factor_list = []
for i, smoke in enumerate(smoke_list):
    smoke_num = i+1
    newdf = df[(df['SMOKE'] == smoke_num)] 
    factor_list.append((sum(newdf['MICHD'])/len(newdf['MICHD']))*100.)
fac_dict['smoke'] = dict(zip(smoke_list,factor_list))
factor_list = []
for i, todo in enumerate(todo_list):
    todo_num = i+1
    newdf = df[(df['_TOTINDA']== todo_num)]
    factor_list.append((sum(newdf['MICHD'])/len(newdf['MICHD']))*100.)
fac_dict['todo'] = dict(zip(todo_list,factor_list))
factor_list = []
for i, hcov in enumerate(hcov_list):
    hcov_num = i+1
    df[(df['_HCVU651']== hcov_num)]
    factor_list.append((sum(newdf['MICHD'])/len(newdf['MICHD']))*100.)
fac_dict['hcov'] = dict(zip(hcov_list,factor_list))
factor_list = []
for sleep in sleep_list:
    sleep_num = int(sleep)
    newdf = df[(df['SLEPTIM1']== sleep_num)] 
    factor_list.append((sum(newdf['MICHD'])/len(newdf['MICHD']))*100.)
fac_dict['sleep'] = dict(zip(sleep_list,factor_list))
factor_list = []
for i, drink in enumerate(drink_list):
    drink_num = i+1
    newdf =  df[(df['_RFDRHV7']== drink_num)]
    factor_list.append((sum(newdf['MICHD'])/len(newdf['MICHD']))*100.)
fac_dict['drink'] = dict(zip(drink_list,factor_list))
factor_list = []
for i, diab in enumerate(diab_list):
    diab_num = i 
    newdf = df[(df['DIABETE4']== diab_num)]
    factor_list.append((sum(newdf['MICHD'])/len(newdf['MICHD']))*100.)
fac_dict['diab'] = dict(zip(diab_list,factor_list))         
            
pickle.dump(fac_dict, open('factors', 'wb'))
