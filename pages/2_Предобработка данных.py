import streamlit as st
import pandas as pd
import numpy as np

data2= pd.read_csv("neo_task.csv")
df2 = pd.DataFrame(data2)

st.title('Предобработка данных')

st.header('Предобработка датасета для задачи классификации')
st.markdown('---')
st.dataframe(df2)

st.markdown('Вывод числа пропущенных значений')
code = '''
data.isna().sum().sort_values(ascending=False)
'''
st.code(code, language='python')

st.code(data2.isna().sum().sort_values(ascending=False))

