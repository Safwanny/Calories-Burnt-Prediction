# Calories-Burnt-Prediction
Regression Model using XGBoost and Neural Network for predicting calories burnt during exercise

There is another Neural Network model in the code using tensorFlow, it a play around to compare the accuracies of a Neural Network with
different paramenter and settings also against the XGBRegressor.

Merged teh two different csv files into one file.
Conducted data exploration for better understanding the trends in the data and features using plots and heatmaps.
removed features that were not requied for training.
converted all features to int64 (dummy variables and also replace)

fitted two different models for personal performance study
used many metrics to evaluate the performance of respeetive models

created function that predicts self input values 

used streamlit and pickle libraries to deploy the models

issue: using the XBG model, when predicting for large input values (eg time = 200 mins) the model seems to flatten out at around 250-300
