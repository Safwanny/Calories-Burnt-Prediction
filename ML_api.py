#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 07:25:00 2025

@author: safwanshaikh
"""

from fastapi import FastAPI
from pydantic import BaseModel   # purpose is to setup the model in which data is to be posted
import pickle

app = FastAPI()

class model_input(BaseModel):
    
    Gender : int         # format of data to be expected by the api
    Age : int
    Height : float
    Weight : float    
    Duration : float
    Heart_Rate : int
    Body_Temp : float
    
# loading the saved model
with open('trained_model_NN.sav', 'rb') as model_file:
    calories_model_NN = pickle.load(model_file)

#calories_model = pickle.load(open('trained_model.sav'), 'rb')

@app.post('/calories_prediction')       # used when one has to give values to the API (model_input data will be posted to the app - endpoint calories_prediction )

def calories_pred(input_param : model_input):   # values user will give
    
    input_dictionary = input_param.dict()
    
    gender = input_dictionary['Gender']      # extracting each value from the json dictionary
    age = input_dictionary['Age']
    height = input_dictionary['Height']
    weight = input_dictionary['Weight']
    dur = input_dictionary['Duration']
    bmp = input_dictionary['Heart_Rate']
    temp = input_dictionary['Body_Temp']
    
    input_list = [gender, age, height, weight, dur, bmp, temp]
    
    prediction = calories_model_NN.predict([input_list])   # input_list is a list enclosed in a list so that the need for reshaping is not required
    
    return {"predicted_calories": float(prediction[0])}
    
 # run uvicorn MLNN.api:app - following code on terminal to get URL