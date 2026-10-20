import streamlit as st
import requests

import numpy as np
import pandas as pd

"""
# Zoologist front
"""


island = st.selectbox('Select island', ['Biscoe', 'Dream', 'Torgersen'])
bill_length = st.number_input('Enter the bill length (in mm)', format="%d", step=1)
bill_depth = st.number_input('Enter the bill depth (in mm)')
flipper_length = st.number_input('Enter the flipper length (in mm)')
body_mass = st.number_input('Enter the body mass (in g)')
sex = st.selectbox('Select sex', ['Male', 'Female'])

if st.button("Predict species"):
    url = st.secrets['API_URL']
    params = {
        'island': island,
        'bill_length_mm': bill_length,
        'bill_depth_mm': bill_depth,
        'flipper_length_mm': flipper_length,
        'body_mass_g': body_mass,
        'sex': sex
    }

    response = requests.get(f'{url}/predict', params=params)

    if response.status_code == 200:
        prediction = response.json()
        species = prediction['species'] if 'species' in prediction else prediction['prediction']
        st.markdown(f'Predicted species: {prediction['prediction']}')

    else:
        st.error(f'API call failed with status {response.status_code}: {response.text}')
