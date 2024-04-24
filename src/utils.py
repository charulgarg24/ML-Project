import os
import sys
import numpy as np
import pandas as pd
import dill
from sklearn.metrics import r2_score
from src.exception import CustomException
from sklearn.model_selection import GridSearchCV

def save_object(file_path,obj):
    try:

        dir_oath=os.path.dirname(file_path)  # it is  the file_path
        os.makedirs(dir_oath, exist_ok=True)  # create directory of particular fiel apth
        with  open(file_path,"wb" )as file_obj: # then we go ahead and dump it 
            dill.dump(obj,file_obj)
    
    except Exception as e:
        raise CustomException(e,sys)

def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):   # it will iterate over each adne very model
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]
            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)
            # model.fit(X_train,y_train) # fir on x_trainy,y_train

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train) # prediction on x_train

            y_test_pred = model.predict(X_test) # prediction on x_test


            train_model_score = r2_score(y_train, y_train_pred)  # here r2 score is used to predict data 

            test_model_score = r2_score(y_test, y_test_pred)  # here we are using r2 score to t4est the model 

            report[list(models.keys())[i]] = test_model_score  # than we will keep on update that test predicted value in this report this is my list 

        return report

    except Exception as e:
        raise CustomException(e, sys)
# it is responsible for ;aoding the pickle file we are writing it in utils file bcz it is common fucntionairy 
def load_object(file_path):  # it will open the file path in read byte mode and it is loading the pickel file using the dill thts why we import dill
    try:
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)