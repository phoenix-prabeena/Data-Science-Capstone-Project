import streamlit as st
import pandas as pd
import pickle
import numpy as np

with open('best_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title of the app
st.title('Car Selling Price Prediction')

# User input section
st.header('Input Features')

year = st.number_input('Year of Purchase', min_value=1992, max_value=2020, step=1)
km_driven = st.number_input('Kilometers Driven', min_value=1, step=100)
fuel = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])
seller_type = st.selectbox('Seller Type', ['Individual', 'Dealer', 'Trustmark Dealer'])
transmission = st.selectbox('Transmission Type', ['Manual', 'Automatic'])
owner = st.selectbox('Owner Type', ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner'])

# Create a DataFrame for the input features
input_data = pd.DataFrame({
    'year': [year],
    'km_driven': [km_driven],
    'fuel': [fuel],
    'seller_type': [seller_type],
    'transmission': [transmission],
    'owner': [owner]
})


if st.button('Predict'):
    if fuel == 'Diesel':
        fuel = 1
    elif fuel == 'Petrol':
        fuel = 4
    elif fuel == 'CNG':
        fuel = 0
    elif fuel == 'LPG':
        fuel = 3
    else:
        fuel = 2
   
    if seller_type == 'Individual':
        seller_type = 1
    elif seller_type == 'Dealer':
        seller_type = 0
    else:
        seller_type = 2
   
    if transmission == 'Manual':
        transmission = 1
    else:
        transmission = 0

    if owner == 'First Owner':
        owner = 0
    elif owner == 'Second Owner':
        owner = 2
    elif owner == 'Third Owner':
        owner = 4
    elif owner == 'Fourth & Above Owner':
        owner = 1
    else:
        owner = 3
       
    
    test = np.array([year, km_driven, fuel, seller_type, transmission, owner])
    test = test.reshape(1, -1)


    prediction = model.predict(test)[0]

    # Display the result
    st.success(f'Predicted Price in Rupees from Actual: {prediction}')
