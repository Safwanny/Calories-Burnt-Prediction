#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 17:49:48 2025

@author: safwanshaikh
"""

import numpy as np
import pickle
import streamlit as st

# Loading the saved data
loaded_model = pickle.load(open('/Users/safwanshaikh/Downloads/AML/Calories-Burnt-Prediction/trained_model_NN.sav', 'rb'))

# Creating a function for prediction
def CaloriesBurnt_prediction(input):

    input_numpy = np.asarray(input)  # converting input to numpy
    input_reshape = input_numpy.reshape(1,-1)  # reshaping the array to predict one instance

    input_prediction = loaded_model.predict(input_reshape)

    return input_prediction


def main():
    
    # giving a title
    st.title('Calories Burnt Prediction WebApp')
    
    # taking in the input data
    Gender = st.text_input('Gender (male:0, female:1): ')
    Age = st.text_input('Age: ')
    Height = st.text_input('Height(cm): ')
    Weight = st.text_input('Weight(kg): ')
    Duration = st.text_input('Workout Duration(mins): ')
    Heart_Rate = st.text_input('Average Heart Rate: ')
    Body_Temp = st.text_input('Average Body Temperature: ')
        
    # code for prediction
    result = ''
    
    # creating a button for prediction
    if st.button('Predict Calories Burnt'):
        try:
            # Converting input values to appropriate data types
            Gender = int(Gender)
            Age = int(Age)
            Height = float(Height)
            Weight = float(Weight)
            Duration = float(Duration)
            Heart_Rate = int(Heart_Rate)
            Body_Temp = float(Body_Temp)
            
            # Making prediction
            result = CaloriesBurnt_prediction([Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp])
            
            st.success(f"Predicted Calories Burnt: {result[0]}")
        except ValueError:
            st.error("Please enter valid numeric values for all fields.")
    

if __name__ == '__main__':    # this makes sure that this code (main) will only run if this file is called on stand alone
    main()
    
    
# this code will not run through the IDE but you have to use the anaconda command prompt