import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from datapreprocessing.preprocess import Data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score
import pandas as pd

PATH=r'C:\Users\kriti\DatingSpeedMatch\data\speed_dating_master.csv'
df=pd.read_csv(PATH)

x=df.drop(['event_id','male_id','female_id','match'],axis=1)
y=df['match']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

preprocessed=Data()
preprocessed_transform=preprocessed.preprocess_data(x_train)

x_train=preprocessed_transform.fit_transform(x_train)
x_test=preprocessed_transform.transform(x_test)

models={
    'logisitic_Reg':LogisticRegression(),
    'desicion Tree':DecisionTreeClassifier(),
    'Random Forest':RandomForestClassifier(),
    

}

import mlflow
for name,algo in models.items():
   mlflow.set_experiment('Dating Speed Match')
   with mlflow.start_run():
    # model=LogisticRegression()
    algo.fit(x_train,y_train)
    y_pred=algo.predict(x_test)
    acc_score=accuracy_score(y_test,y_pred)
    precision=precision_score(y_test,y_pred,pos_label=1)
    recall=recall_score(y_test,y_pred,pos_label=1)
    score=f1_score(y_test,y_pred,pos_label=1)

    #storing into the model metrics
    mlflow.log_metric('acc',acc_score)
    mlflow.log_metric('pre',precision)
    mlflow.log_metric('recall',recall)
    mlflow.log_metric('f1',score)


    #logging the model
    mlflow.sklearn.log_model(sk_model=algo,name=name)

    print(f'model {name} save succesfully')


# model=LogisticRegression()
# model.fit(x_train,y_train)
# y_pred=model.predict(x_test)
# score=accuracy_score(y_test,y_pred)
# print(score)

# f1=f1_score(y_test,y_pred)
# print(f1)
# import numpy as np

# print(np.isnan(x_train).sum())
# print(np.isnan(x_test).sum())
