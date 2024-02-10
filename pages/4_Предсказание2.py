import pandas as pd 
import numpy as np 
import math
import pickle
from sklearn.model_selection import train_test_split 
import streamlit as st 


df= pd.read_csv('Data_preprocessed.csv')

if df is not None:
    st.header("Датасет")
    st.dataframe(df)
    st.write("---")
    st.title("Hazardous Prediction") 

    list=[]

    for i in df.columns[:-1]:
        a = st.slider(i,int(df[i].min()), int(math.ceil(df[i].max())),int(df[i].max()/2))
        list.append(a)

    list = np.array(list).reshape(1,-1)
    list=list.tolist()
    st.title("Тип модели обучения: kNN")
    

    button_clicked = st.button("Предсказать")
    if button_clicked:
        with open('models/knn.pkl', 'rb') as file:
            knn_model = pickle.load(file)
        if knn_model.predict(list) == 0:
            st.success("Объект не опасен")
        else:
            st.success("Объект опасен")
