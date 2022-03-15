"""
@author: ELMASRY
"""
import streamlit as st 
import joblib


def main():
    html_temp =""""
    <div style = "background-color:lightblue;padding:16px">
     <h2 style="color:black;text-align:center"> Diabetes Prediction App </h2>
    </div>
    
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    model = joblib.load('Diabetes_model')
    p1 =st.number_input('Enter Number of Pregnancies ',0,20)
    p2 =st.number_input('Enter Glucose Value ',0)
    p3 =st.number_input('Enter BloodPressure Value ',)
    p4 =st.number_input('Enter SkinThickness Value ')
    p5 =st.number_input('Enter Insulin Value')
    p6 =st.number_input('Enter BMI Value')
    p7 =st.number_input('Enter DiabetesPedigreeFunction Value between 0 and 1')
    p8 =st.number_input('Enter Your Age',10,100)
    
    if st.button('Predict'):
        pred = model.predict([[p1,p2,p3,p4,p5,p6,p7,p8]])
        
        st.success('prediction is   {}'.format(pred[0]))
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    main()
    #