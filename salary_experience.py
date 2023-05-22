# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 17:06:05 2023

@author: sande
"""




import pandas as pd

import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open("D:\salary Exp Simple linear regration\salary_experience.pkl", 'rb'))


    
    

def main():
     # giving a title
    st.title('Salary  Prediction')
    
    
    # getting the input data from the user
    
    
    No_of_Experience = st.text_input('YearsExperience')
    
    
    
    
    # code for Prediction
    price = ''
    
    # creating a button for Prediction
    
    if st.button('Predict Price'):
        
        price=loaded_model.predict(pd.DataFrame([[No_of_Experience]],columns=['YearsExperience']))

        
    st.success(price)
    
    
    
if __name__ == '__main__':
    main()