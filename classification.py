import numpy as np
import pandas as pd
from datetime import datetime
from dateutil import parser
import scipy.stats
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

# Reading data from CSV file
df=pd.read_csv("C:/Users/MOHIT/Desktop/AV/Train.csv")
df1=pd.read_csv("C:/Users/MOHIT/Desktop/AV/Test.csv")
data = pd.concat([df,df1], ignore_index=True)
df=data.copy()

# Replacing missing values in the dataset
for i in df.columns:
    df[i].fillna(df[i].mode()[0],inplace=True)

# Data parsing and processing
df['new_Manager_Grade']=df['Manager_Grade'].fillna(np.mean(df['Manager_Grade']))
df['Manager_Grade']=pow((df['Manager_Grade']),0.333)

df.loc[df['Manager_Num_Coded']>4,'Manager_Num_Coded']=4
df['Manager_Coded']=df['Manager_Num_Coded'].fillna(df['Manager_Num_Coded'].mode()[0])

df.loc[df['Manager_Business']<0,'Manager_Business']=np.abs(df['Manager_Business'])
df['Manager_Business']=df['Manager_Business'].fillna(np.mean(df['Manager_Business']))
j=0
for i in df['Manager_Business']:
    if i!=0:
         df.loc[df.index[j], 'Manager_Business'] = np.log(i)
    else:
        df.loc[df.index[j], 'Manager_Business'] = i
    j=j+1

df.loc[(df['Manager_Business'] > 0) & (df['Manager_Business'] < 10), ['Manager_Business']]=9
df.loc[(df['Manager_Business'] > 10) & (df['Manager_Business'] < 11), ['Manager_Business']]=10
df.loc[(df['Manager_Business'] > 11) & (df['Manager_Business'] < 12), ['Manager_Business']]=11
df.loc[(df['Manager_Business'] > 12) & (df['Manager_Business'] < 13), ['Manager_Business']]=12
df.loc[(df['Manager_Business'] > 13) & (df['Manager_Business'] < 14), ['Manager_Business']]=13
df.loc[(df['Manager_Business'] > 14) , ['Manager_Business']]=14

df['Manager_Num_Products']=df['Manager_Num_Products'].fillna(np.mean(df['Manager_Num_Products']))
df['Manager_Num_Products']=pow((df['Manager_Num_Products']),0.3333)

df['Manager_Business2']=pow((df['Manager_Business2']),0.3333)
df['Manager_Num_Products2']=pow((df['Manager_Num_Products2']),0.3333)

df['Application_Receipt_Date'] = df['Application_Receipt_Date'].astype('datetime64[ns]')
j=0
for i in df['Application_Receipt_Date']:
    df.loc[df.index[j],'Application_Receipt_Date'] = parser.parse(i)
    j=j+1

df['Applicant_Gender'].replace("F",0,inplace=True)
df['Applicant_Gender'].replace("M",1,inplace=True)

df['Applicant_BirthDate']=df['Applicant_BirthDate'].fillna(df['Applicant_BirthDate'].mode()[0])
j=0
for i in df['Applicant_BirthDate']:
    df.loc[df.index[j],'Applicant_BirthDate'] = parser.parse(i)
    j=j+1

df['Applicant_Marital_Status']=df['Applicant_Marital_Status'].fillna('S')
df.loc[df['Applicant_Marital_Status']=='W','Applicant_Marital_Status']='S'
df.loc[df['Applicant_Marital_Status']=='D','Applicant_Marital_Status']='S'
df['Applicant_Marital_Status'].replace("S",0,inplace=True)
df['Applicant_Marital_Status'].replace("M",1,inplace=True)

df['Applicant_Occupation']=df['Applicant_Occupation'].fillna('Others')
df["Applicant_Occupation"] = df["Applicant_Occupation"].astype('category')
df["Applicant_Occupation"] = df["Applicant_Occupation"].cat.codes

df['Applicant_Qualification']=df['Applicant_Qualification'].fillna('Others')
df['Applicant_Qualification']=df['Applicant_Qualification'].str.strip()
df.loc[(df['Applicant_Qualification']!='Class XII') & (df['Applicant_Qualification']!='Graduate') & (df['Applicant_Qualification']!='Class X')& (df['Applicant_Qualification']!='Masters of Business Administration'),'Applicant_Qualification']= 'Others'
df["Applicant_Qualification"] = df["Applicant_Qualification"].astype('category')
df["Applicant_Qualification"] = df["Applicant_Qualification"].cat.codes

j=0
for i in df['Manager_DOJ']:
    df.loc[df.index[j],'Manager_DOJ'] = parser.parse(i)
    j=j+1

df.loc[df['Manager_Joining_Designation']=='Other','Manager_Joining_Designation']=df['Manager_Joining_Designation'].mode()[0]
valid_level=['Level 1','Level 2','Level 3','Level 4','Level 5']
df.loc[~df['Manager_Joining_Designation'].isin(valid_level),'Manager_Joining_Designation']='Level 5'
df["Manager_Joining_Designation"] = df["Manager_Joining_Designation"].astype('category')
df["Manager_Joining_Designation"] = df["Manager_Joining_Designation"].cat.codes

df["Manager_Current_Designation"] = df["Manager_Current_Designation"].astype('category')
df["Manager_Current_Designation"] = df["Manager_Current_Designation"].cat.codes

df['Manager_Status'].replace("Confirmation",0,inplace=True)
df['Manager_Status'].replace("Probation",1,inplace=True)

df['Manager_Gender'].replace("F",0,inplace=True)
df['Manager_Gender'].replace("M",1,inplace=True)

j=0
for i in df['Manager_DoB']:
    df.loc[df.index[j],'Manager_DoB'] = parser.parse(i)
    j=j+1

# Creating a shallow copy of the original dataframe, so that the new temporary dataframe can be manipulated and given as input to the classifiers
df2=df.copy()
drop_columns=['ID']
df2.drop(drop_columns,axis=1,inplace=True)

# Train and test data splitting
Uncorrelated_Features=['Application_Receipt_Date','Applicant_BirthDate','Manager_DOJ','Manager_DoB']
df2=df2.drop(Uncorrelated_Features, axis=1)
y=data['Business_Sourced'].dropna()
x=df2
x=x.drop('Business_Sourced',axis=1)
x1=x.dropna()[:9527]
x_validation=x[9527:]
IDs=df['ID']
IDs=np.array(IDs[9527:])
x_train, x_test,y_train,y_test = train_test_split(x1,y, test_size=0.25, random_state=42)

# Creating the Random Forest Classifier with parameters obtained by hyper parameter tuning
RF = RandomForestClassifier(n_estimators= 1000, min_samples_split=10, min_samples_leaf=2,max_features='sqrt',max_depth= 10, bootstrap= True)

# Hyper Parameter tuning of the Random Forest
'''
# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]
# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}

rf_random = RandomizedSearchCV(estimator = logisticRegr, param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = 1)
rf_random.fit(x_train, y_train)
print(rf_random.best_params_)
'''

# Fitting the Random Forest classifier
RF.fit(x_train, y_train)
prediction = RF.predict(x_test)

# Classifying the test data
score=RF.score(x_test,y_test)
predictions2 = RF.predict_proba(x_test)
final_predicion=RF.predict(x_validation)
final_predicion=np.array(final_predicion)

final_df=pd.DataFrame(final_predicion,index=IDs,columns=['Business_Sourced'])
final_df['ID'] = final_df.index
final_col_names=['ID','Business_Sourced']
final_df=final_df[final_col_names]
final_df.reset_index(drop=True,inplace=True)

# Writing test data results to output CSV file
final_df.to_csv('C:/Users/MOHIT/Desktop/AV/Classification_Soln.csv', encoding='utf-8', index=False)
