import streamlit as st
import pandas as pd
import pickle

st.title('Iris Prediction')
st.write('My first streamlit application')

sl = float(st.number_input('Enter Sepal Length'))
sw = float(st.number_input('ENter Sepal Width'))
pl = float(st.number_input('Enter Petal length'))
pw = float(st.number_input('Enter Petal Width'))

if st.button('Predict?'):
    st.write('Processing')
    st.write('Please build your logic here!!!')
    with open('model.pkl', 'rb') as models:
        pred_model = pickle.load(models)
    predicted_value = pred_model.predict([[sl, sw, pl, pw]])
    st.write(f'Predicted value is {predicted_value}')