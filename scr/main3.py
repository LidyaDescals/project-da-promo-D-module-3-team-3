# Tratamiento de datos
# -----------------------------------------------------------------------
import numpy as np
import pandas as pd


# Codificación variables categóricas
# ------------------------------------------------------------------------------
from sklearn.preprocessing import OneHotEncoder


# Modelado y evaluación
# ------------------------------------------------------------------------------
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn import tree
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import GridSearchCV
import streamlit as st
import pickle
import os
pd.options.display.max_columns = None


def prediccion(month, year, weekday, workingday, holiday, weathersit, temp, hum, windspeed):
    with open("scr/estandarizacion.pkl", "rb") as estandarizacion:
        scaler = pickle.load(estandarizacion)

    with open("scr/mejor_modelo.pkl", "rb") as modelo:
        bosque = pickle.load(modelo)

    df_pred = pd.DataFrame({"month": [month], "year": [year], "weekday": [weekday], "workingday": [workingday], "holiday": [holiday], "weathersit": [weathersit], "temp": [temp], "hum": [hum], "windspeed": [windspeed]})
    df_pred[['month', 'year', 'weekday', 'workingday', 'holiday', 'weathersit']] = df_pred[['month', 'year', 'weekday', 'workingday', 'holiday', 'weathersit']].astype("category")
    pred_num = df_pred.select_dtypes(include=np.number)
    X_escaladas = scaler.transform(pred_num)
    num_estandar = pd.DataFrame(X_escaladas, columns=pred_num.columns)
    df_pred[num_estandar.columns] = num_estandar

    mapa_month = {7: 9.67, 11: 6.64, 0: 5.69, 6: 9.65, 2: 8.13, 4: 9.54, 9: 9.2, 3: 8.47, 5: 9.63, 10: 7.61, 8: 9.82, 1: 5.95}
    mapa_year = {2018: 4, 2019: 6, 2020: 6, 2021: 6, 2022: 6, 2023: 6, 2024: 6, 2025: 6}
    mapa_weekday = {0: 13.82, 1: 13.98, 4: 14.77, 5: 14.59, 6: 14.37, 3: 14.54, 2: 13.9}
    mapa_holiday = {0: 4, 1: 3}
    mapa_weathersit = {1: 4, 2: 3, 3: 1}

    categoricas = df_pred.select_dtypes(include="category")
    categoricas.drop(["workingday"], axis=1, inplace=True)
    lista_mapas = [mapa_month, mapa_year, mapa_weekday, mapa_holiday, mapa_weathersit]

    for indice, col in enumerate(categoricas):
        df_pred[col] = df_pred[col].map(lista_mapas[indice])

    df_pred["workingday_0"] = 1 if workingday == 0 else 0
    df_pred["workingday_1"] = 1 if workingday == 1 else 0

    df_pred.drop(["workingday"], axis=1, inplace=True)

    prediction = bosque.predict(df_pred)
    cnt = prediction[0]
    return cnt

def main():
    st.image('scr/datalicious.png')
    st.image('scr/bici.png')
    st.title("Predicción de alquiler de bicicletas")


    # meses = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # dias_semana = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    mes = st.select_slider('Mes', ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"))

    if mes == "Enero":
	    month = 0
    if mes == "Febrero":
	    month = 1
    if mes == "Marzo":
	    month = 2
    if mes == "Abril":
	    month = 3
    if mes == "Mayo":
	    month = 4
    if mes == "Junio":
	    month = 5
    if mes == "Julio":
	    month = 6
    if mes == "Agosto":
	    month = 7
    if mes == "Septiembre":
	    month = 8
    if mes == "Octubre":
	    month = 9
    if mes == "Noviembre":
	    month = 10
    if mes == "Diciembre":
	    month = 11
   
    year = st.slider("Año", 2018, 2025)
    dia = st.select_slider("Día de la semana", ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"))


    if dia == "Lunes":
	    weekday = 0
    if dia == "Martes":
	    weekday = 1
    if dia == "Miércoles":
	    weekday = 2
    if dia == "Jueves":
	    weekday = 3
    if dia == "Viernes":
	    weekday = 4
    if dia == "Sábado":
	    weekday = 5
    if dia == "Domingo":
	    weekday = 6

    laborable = st.selectbox("Día laborable", ("No", "Sí"))

    if laborable == "No":
	    workingday = 0
    if laborable == "Sí":
	    workingday = 1

	
    festivo = st.selectbox("Día festivo", ("No", "Sí"))

    if festivo == "No":
	    holiday = 0
    if festivo == "Sí":
	    holiday = 1

    tiempo = st.select_slider("Clima", ("Cielo despejado o parcialmente nublado", "Niebla, cielo muy nublado", "Lluvia o nieve ligeras"))

    if tiempo == "Cielo despejado o parcialmente nublado":
	    weathersit = 1
    if tiempo == "Niebla, cielo muy nublado":
	    weathersit = 2
    if tiempo == "Lluvia o nieve ligeras":
	    weathersit = 3
		
    temp = st.slider("Temperatura en grados Celsius", 0, 35)
    hum = st.slider("Porcentaje de humedad", 0, 100)
    windspeed = st.slider("Velocidad del viento en km/h", 0 , 35)
    


    if st.button("Predecir"):
        prediction = prediccion(month, year, weekday, workingday, holiday, weathersit, temp, hum, windspeed)
        st.success(f"La cantidad de bicicletas alquiladas estimada es: {int(prediction)}")
	

if __name__ == '__main__':
    main()


