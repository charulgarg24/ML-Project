##  to predict new data
  ## i wil try to create a simple web application which deal with pickel file  let say there is a form in which we fill a form of student performance 
# then we click on submit  internally bakcend will capture the data than need to be probalble attract with need of data pickel of data  and then we are goin to see the preiction
  # in this we are goign to see about prediction pipeline part
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object # to load pickel file

class PredictPipeline:  # class prediction pipeline
    def __init__(self):
        pass
    def predict(self,features):
        try:    
            model_path='artifacts\model.pkl'
            preprocessor_path='artifacts\preprocessor.pkl'
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scale=preprocessor.transform(features)  # IT IS USED FOR SCAILING AND TRNASFORM FEATURE 
            predicts=model.predict(data_scale)
            return predicts
        except Exception as e:
            raise CustomException(e,sys)

        
class CustomData :         # this will be helpfull in mapping to all the input we ARE gicing in the html to bakcned with it's [partiualr value]
    def __init__(self,
        gender:str,
        race_ethnicity:str,
        parental_level_of_education,
        lunch:str,
        test_preparation_course:str,
        reading_score:int,
        writing_score:int):
         # creating variable using self
        self.gender = gender
        self.race_ethnicity= race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score
    
    def get_data_as_data_frame(self):  # it will return all my inout in the formof dataframe
        try:
            custom_data_input_dict={
                "gender":[self.gender],
                "race_ethnicity":[self.race_ethnicity],
                "parental_level_of_education" : [self.parental_level_of_education],
                "lunch":[self.lunch],
                "test_preparation_course":[self.test_preparation_course],
                "reading_score":[self.reading_score],
                "writing_score":[self.writing_score]

            }
            return pd.DataFrame(custom_data_input_dict)  # what will happend is that from web application the input that we are giving same input will get map to the particular value 
        except Exception as e:
            raise CustomException(e,sys)

