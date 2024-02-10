import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data= pd.read_csv("energy_task_preprocessed.csv")

st.title('Визуализация датасета')

st.header('Датасет для регрессии - "Кол-во включенных электроприборов"')

st.markdown('---')

st.write("Тепловая карта по матрице корреляции между признаками:")


correlation_matrix = data.corr()

st.code(correlation_matrix, language='python')

fig = sns.heatmap(correlation_matrix, annot=True, cmap="YlGnBu", fmt=".2f")

st.pyplot(fig)

st.write("Диаграмма рассеяния для электроприборов и освещения")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Appliances", "lights"])
st.scatter_chart(chart_data)

st.write("Гистограмма предсказываемого признака")

fig, ax = plt.subplots()
ax.hist(data['Appliances'], bins=20)

st.pyplot(fig)