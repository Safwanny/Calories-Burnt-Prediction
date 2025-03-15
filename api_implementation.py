#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 08:54:16 2025

@author: safwanshaikh
"""

import json 
import requests

url = 'http://127.0.0.1:8000/calories_prediction'

input_data_for_model = {
    'Gender': 0,
    'Age': 21,
    'Height': 181.0, 
    'Weight': 94.0,
    'Duration': 80.0,
    'Heart_Rate': 136,
    'Body_Temp': 60.0,
}

# Set the correct headers for JSON content
headers = {'Content-Type': 'application/json'}   # header are required for type specification and API interpretation

# Convert dict to JSON string
input_json = json.dumps(input_data_for_model)

# Make the request
response = requests.post(url, data=input_json, headers=headers)

# Print the response
print(response.text)