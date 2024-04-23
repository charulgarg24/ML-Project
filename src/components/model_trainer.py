## all model training code here
# @ what is your faourite algorithm 
#  ANS i dont' have any favourite algorithm you ask me i wil be happy to answer that

import os
import sys
from dataclasses import dataclass
from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from xgboost import  XGBRegressor
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_models
# starting the model training part
@dataclass  #When you decorate a class with @dataclass, Python automatically generates special methods such as __init__, __repr__, __eq__, and __hash__ based on the class variables defined within it. This saves you from having to write these methods manually, reducing boilerplate code.

# Here's a brief explanation of what each of these generated methods does:

# __init__: Initializes the object with values for its attributes.
# __repr__: Returns a string representation of the object, suitable for debugging and logging.
# __eq__: Compares two objects for equality based on their attribute values.
# __hash__: Computes a hash value for the object, necessary for using it as a key in hash-based data structures like dictionaries and sets.
class ModelTrainerconfig: # this aprt will basically ahve all the data with respect to the input that we all need input
    trained_model_file_path=os.path.join("artifacts",'model.pkl')    # file path of trai ning model

class  ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerconfig()    # class for

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],   # we have split train and test data
                test_array[:,-1]
            )
            models={
                "Random Forest" : RandomForestRegressor(),
                "Decision Tree" : DecisionTreeRegressor(),
                "Linear Regression": LinearRegression(),
                "Gradient Boosting" : GradientBoostingRegressor(),
                "AdaBoost Regressor" : AdaBoostRegressor(),
                # "K-Neighbours Classifier" : KNeighborsRegressor(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor" :  CatBoostRegressor(verbose=False),
            }
                    # now we will see which modelis performing well 

                    # we will define this evaluate fucntion in utils.py
            # here we ahve addedd the parameter for hyperparamter tunning
            params={
                "Decision Tree": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    # 'splitter':['best','random'],
                    # 'max_features':['sqrt','log2'],
                },
                "Random Forest":{
                    # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                 
                    # 'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Gradient Boosting":{
                    # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    # 'criterion':['squared_error', 'friedman_mse'],
                    # 'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Linear Regression":{},
                "XGBRegressor":{
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "CatBoosting Regressor":{
                    'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "AdaBoost Regressor":{
                    'learning_rate':[.1,.01,0.5,.001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]
                }
                
            }
        

            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,  
                                             models=models,param=params)  # in this we are passing the parameter
            
            ## To get the best model score from dict
            best_model_score=max(sorted(model_report.values()))
            ## To get the best model score from dict
            best_model_name = list(model_report.keys())[    # here we are getting our model anem because our lkey ismodel anme 
                list(model_report.values()).index(best_model_score)
            ]
            best_model=models[best_model_name]
            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info(f"best found model on both training and testing dataset")
# now we will inport preprocessing pickel fielt o basically dodata transformation or naything u need to do 
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
                )
            predicted=best_model.predict(X_test)
            r2_square = r2_score(y_test, predicted)
            return r2_square

        except Exception as e:
            return CustomException(e,sys)    
