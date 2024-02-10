from matplotlib import pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np

data= pd.read_csv("energy_task.csv")
data = pd.DataFrame(data)

st.title('Предобработка данных')

st.header('Предобработка датасета для задачи регрессии')
st.markdown('---')
st.dataframe(data)

st.markdown('Вывод числа пропущенных значений:')
code = '''
data.isna().sum().sort_values(ascending=False)
'''
st.code(code, language='python')

st.code(data.isna().sum().sort_values(ascending=False))

st.markdown('Вывод головы датасета:')
code = '''
data.head()
'''
st.code(code, language='python')
st.dataframe(data.head(5))

st.markdown('Удалим столбцы, не несущие какую-либо информацию для обучения модели:')
code = '''
data = data.drop(['date'], axis = 1)

'''
data = data.drop(['date'], axis = 1)
st.code(code, language='python')

st.dataframe(data.head(5))

st.markdown('Вывод статистической сводки по датасету:')

data_descr = data.describe()

st.dataframe(data_descr)

st.markdown('Заполнение пропущенных значений в интервале от минимального до максимального')

code = '''
energy['T_out'] = energy['T_out'].map(lambda x: np.random.randint(-5, 26.1) if pd.isna(x) else x)
energy['RH_2'] = energy['RH_2'].map(lambda x: np.random.randint(17.2, 29) if pd.isna(x) else x)
energy['Press_mm_hg'] = energy['Press_mm_hg'].map(lambda x: np.random.randint(729, 772) if pd.isna(x) else x)
energy['T8'] = energy['T8'].map(lambda x: np.random.randint(16, 27) if pd.isna(x) else x)
energy['RH_out'] = energy['RH_out'].map(lambda x: np.random.randint(24, 100) if pd.isna(x) else x)
energy['RH_5'] = energy['RH_5'].map(lambda x: np.random.randint(-6, 28) if pd.isna(x) else x)
energy['T9'] = energy['T9'].map(lambda x: np.random.randint(15, 25) if pd.isna(x) else x)
energy['RH_6'] = energy['RH_6'].map(lambda x: np.random.randint(1, 100) if pd.isna(x) else x)
energy['RH_4'] = energy['RH_4'].map(lambda x: np.random.randint(28, 51) if pd.isna(x) else x)
energy['T7'] = energy['T7'].map(lambda x: np.random.randint(1, 66) if pd.isna(x) else x)
energy['Visibility'] = energy['Visibility'].map(lambda x: np.random.randint(1, 66) if pd.isna(x) else x)
energy['RH_9'] = energy['RH_9'].map(lambda x: np.random.randint(29, 53) if pd.isna(x) else x)
'''

data['T_out'] = data['T_out'].map(lambda x: np.random.randint(-5, 26.1) if pd.isna(x) else x)
data['RH_2'] = data['RH_2'].map(lambda x: np.random.randint(17.2, 29) if pd.isna(x) else x)
data['Press_mm_hg'] = data['Press_mm_hg'].map(lambda x: np.random.randint(729, 772) if pd.isna(x) else x)
data['T8'] = data['T8'].map(lambda x: np.random.randint(16, 27) if pd.isna(x) else x)
data['RH_out'] = data['RH_out'].map(lambda x: np.random.randint(24, 100) if pd.isna(x) else x)
data['RH_5'] = data['RH_5'].map(lambda x: np.random.randint(-6, 28) if pd.isna(x) else x)
data['T9'] = data['T9'].map(lambda x: np.random.randint(15, 25) if pd.isna(x) else x)
data['RH_6'] = data['RH_6'].map(lambda x: np.random.randint(1, 100) if pd.isna(x) else x)
data['RH_4'] = data['RH_4'].map(lambda x: np.random.randint(28, 51) if pd.isna(x) else x)
data['T7'] = data['T7'].map(lambda x: np.random.randint(1, 66) if pd.isna(x) else x)
data['Visibility'] = data['Visibility'].map(lambda x: np.random.randint(1, 66) if pd.isna(x) else x)
data['RH_9'] = data['RH_9'].map(lambda x: np.random.randint(29, 53) if pd.isna(x) else x)

st.code(code, language='python')

st.markdown('Гистограмма со значениями целевого признака "Appliances":')

fig, ax = plt.subplots()
ax.hist(data['Appliances'], bins=20)

st.pyplot(fig)

