import streamlit as st
import pandas as pd
import numpy as np

data2= pd.read_csv("neo_task.csv")
df2 = pd.DataFrame(data2)

st.title('Предобработка данных')

st.header('Предобработка датасета для задачи классификации')
st.markdown('---')
st.dataframe(df2)

st.markdown('Вывод числа пропущенных значений:')
code = '''
data.isna().sum().sort_values(ascending=False)
'''
st.code(code, language='python')

st.code(df2.isna().sum().sort_values(ascending=False))

st.markdown('Вывод головы датасета:')
code = '''
data.head()
'''
st.code(code, language='python')
st.dataframe(df2.head(5))


st.markdown('Удалим столбцы, не несущие какую-либо информацию для обучения модели:')
code = '''
data = data.drop(['id', 'name'], axis = 1)

'''
df2 = df2.drop(['id', 'name'], axis = 1)
st.code(code, language='python')

st.dataframe(df2.head(5))

st.markdown('Вывод статистической сводки по датасету:')
code = '''
df2.describe()

'''
data_described = df2.describe()
st.code(code, language='python')

st.dataframe(data_described)

st.markdown('Заполняем пропущенные значения числами в интервале от минимального до максимального:')

code = '''
data['est_diameter_min'] = data['est_diameter_min'].map(lambda x: np.random.uniform(0, 38) if pd.isna(x) else x)
data['est_diameter_max'] = data['est_diameter_max'].map(lambda x: np.random.uniform(0, 84) if pd.isna(x) else x)
data['relative_velocity'] = data['relative_velocity'].map(lambda x: np.random.uniform(203, 230000) if pd.isna(x) else x)
data['miss_distance'] = data['miss_distance'].map(lambda x: np.random.uniform(6745, 74798) if pd.isna(x) else x)
data['absolute_magnitude'] = data['absolute_magnitude'].map(lambda x: np.random.uniform(9, 33) if pd.isna(x) else x)
'''
df2['est_diameter_min'] = df2['est_diameter_min'].map(lambda x: np.random.uniform(0, 38) if pd.isna(x) else x)
df2['est_diameter_max'] = df2['est_diameter_max'].map(lambda x: np.random.uniform(0, 84) if pd.isna(x) else x)
df2['relative_velocity'] = df2['relative_velocity'].map(lambda x: np.random.uniform(203, 230000) if pd.isna(x) else x)
df2['miss_distance'] = df2['miss_distance'].map(lambda x: np.random.uniform(6745, 74798) if pd.isna(x) else x)
df2['absolute_magnitude'] = df2['absolute_magnitude'].map(lambda x: np.random.uniform(9, 33) if pd.isna(x) else x)

st.code(code, language='python') 
st.code(df2.isna().sum().sort_values(ascending=False))
