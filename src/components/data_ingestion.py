## in this we will have code regarding reading the data
import sys
import os
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerconfig
from src.components.model_trainer import ModelTrainer
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artificats',"train.csv")   # it will save our trian.csv filet o this this folder
    test_data_path: str=os.path.join('artificats',"test.csv") 
    raw_data_path: str=os.path.join('artificats',"data.csv") 
    # all these are the inputt hat weare giving to data ingestion part now they were w eaveto save these data

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()  # as i will call thes dataindesgtion class  then these threes path will save to the path

    def initiate_data_ingestion(self):  # if your data is stored in databse then we will write here to read our data from databse
        logging.info("entered the data ingestion method or componenet")
        try:
            df=pd.read_csv('notebook\data\stud.csv')  # reading of the dataset
            logging.info('read the dataset as dataframe')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)# it will gettign teh directory amne woth respect to this path , if it si already there we ahve to keep t no need to delete and create it agian
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)  # we have converted raw data path to cvs
            logging.info("train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42) # train test split
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True) #we are train data to csv and save it 
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True) # we are saving the test data
            logging.info("ingestion of the data is completed")
            return {
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,   # adter this idestion process itwill return this data to next part data trnadformateion
            }
        except Exception as e:
            raise CustomException(e, sys)

if __name__=="__main__":
   obj=DataIngestion()
   train_data,test_data=obj.initiate_data_ingestion()

   data_transformation=DataTransformation()
   train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
   modeltrainer=ModelTrainer()
   print(modeltrainer.initiate_model_trainer(train_arr,test_arr))


