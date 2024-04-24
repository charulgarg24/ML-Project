from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
#application = Flask(__name__): This line creates a Flask application object named application. 
#The Flask() constructor takes the name of the current module (__name__) as an argument. 
#This argument is necessary because Flask uses the name to locate resources such as templates and static files relative to the application module.
# app = application: This line simply assigns the application object to another variable named app. This is a common convention to make the variable name shorter and easier to use.
application = Flask( __name__)   # it give us the entry  point to our application
app=application

# Route for a home apge 
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template("home.html")
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )
        pred_df =data.get_data_as_data_frame()  #   converting all above dataset into dataframe
        print(pred_df)
        Predict_Pipeline=PredictPipeline() # initilaizing predit pipeline
        result=Predict_Pipeline.predict(pred_df)  # it will got ot he predict funtion than 
        return render_template('home.html',result=result[0]) # [0] because basically it will be in list formate
if __name__=='__main__':
    app.run(host="0.0.0.0")