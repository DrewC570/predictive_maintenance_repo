import pandas as pd
import streamlit as st
from sklearn.linear_model import LogisticRegression
from joblib import load

with open("artifacts/model_regression.joblib", "rb") as f:
    predictive_model = load(f)


st.title('Predictive regression model')

voltage = st.slider('select voltage', min_value=97.333603782359, max_value=255.124717259791)
rotation = st.slider('select rotation', min_value=138.432075304341, max_value=695.020984403396)
pressure = st.slider('select pressure', min_value=51.2371057734253, max_value=185.951997730866)
vibration = st.slider('select vibration', min_value=14.877053998383, max_value=76.7910723016723)
age = st.slider('select age', min_value=0, max_value=20)
errors = st.radio('choose an errorID', [1, 2, 3, 4, 5, 'No Error'])
model = st.radio('choose a modelID', [1, 2, 3, 4])


model_dict = {'volt': voltage, 'rotate': rotation, 'pressure': pressure, 'vibration': vibration, 'age': age,
 'error_error1': 0, 'error_error2': 0, 'error_error3': 0, 'error_error4': 0, 'error_error5': 0, 'error_nan': 0,
 'model_model1': 0, 'model_model2': 0, 'model_model3': 0, 'model_model4': 0}

user_df = pd.DataFrame(model_dict, [0])

if errors == 1:
    user_df['error_error1'] = 1
elif errors == 2:
    user_df['error_error2'] = 1
elif errors == 3:
    user_df['error_error3'] = 1
elif errors == 4:
    user_df['error_error4'] = 1
elif errors == 5:
    user_df['error_error5'] = 1
else:
    user_df['error_nan'] = 1

if model == 1:
    user_df['model_model1'] = 1
elif model == 2:
    user_df['model_model2'] = 1
elif model == 3:
    user_df['model_model3'] = 1
elif model == 4:
    user_df['model_model4'] = 1

current_prediction = predictive_model.predict(user_df)

if current_prediction == False:
    st.markdown('There will not be a failure')
else:
    st.markdown('There will be a failure')