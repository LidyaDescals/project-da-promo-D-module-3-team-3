# Tratamiento de datos
# -----------------------------------------------------------------------
import numpy as np
import pandas as pd


# Gráficos
# ------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns


#  Gestión de warnings
# ------------------------------------------------------------------------------
import warnings
warnings.filterwarnings("ignore")


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

pd.options.display.max_columns = None


def prediccion(month, year, weekday, workingday, holiday, weathersit, temp,	hum, windspeed):

    with open("../datos/estandarizacion.pkl", "rb") as estandarizacion:
        scaler = pickle.load(estandarizacion)

    with open("../datos/one_hot.pkl", "rb") as encoding:
        oh = pickle.load(encoding)

    with open("../datos/mejor_modelo.pkl", "rb") as modelo:
        bosque = pickle.load(modelo)
    
    df_pred = pd.DataFrame({"month" : month, "year": year, "weekday": weekday, "workingday": workingday, "holiday": holiday, "weathersit": weathersit, "temp":temp,	"hum":hum, "windspeed":windspeed}, index = [0])
    df_pred[['month', 'year','weekday','workingday','holiday','weathersit']] = df_pred[['month', 'year','weekday','workingday','holiday','weathersit']].astype("category")
    pred_num = df_pred.select_dtypes(include = np.number)
    X_escaladas = scaler.transform(pred_num)
    num_estandar = pd.DataFrame(X_escaladas, columns = pred_num.columns)
    df_pred[num_estandar.columns] = num_estandar

    mapa_month = {'August': 9.67,
    'December': 6.64,
    'January': 5.69,
    'July': 9.65,
    'March': 8.13,
    'May': 9.54,
    'October': 9.2,
    'April': 8.47,
    'June': 9.63,
    'November': 7.61,
    'September': 9.82,
    'February': 5.95}
    mapa_year = {2018: 4, 2019: 6, 2020: 6, 2021: 6, 2022: 6, 2023: 6, 2024: 6, 2025: 6}
    mapa_weekday = {'Monday': 13.82,
    'Tuesday': 13.98,
    'Friday': 14.77,
    'Saturday': 14.59,
    'Sunday': 14.37,
    'Thursday': 14.54,
    'Wednesday': 13.9}
    mapa_holiday = {0: 4, 1: 3}
    mapa_weathersit = {1: 4, 2: 3, 3: 1}

    categoricas = df_pred.select_dtypes(include = "category")
    categoricas.drop(['workingday'], axis = 1, inplace = True)
    lista_mapas = [mapa_month, mapa_year, mapa_weekday,mapa_holiday,  mapa_weathersit ]
    for indice, col in enumerate(categoricas):

        df_pred[col] = df_pred[col].map(lista_mapas[indice])

    
    transformados = oh.transform(df_pred[["workingday"]])
    
    oh_df = pd.DataFrame(transformados.toarray())
    
    oh_df.columns = oh.get_feature_names_out()
    
    df_pred = pd.concat([df_pred, oh_df], axis = 1)

    df_pred.drop("workingday", axis = 1, inplace = True)

    prediction = bosque.predict(df_pred)
    cnt = prediction[0]
    return cnt


def main():
    st.title("Demo de Random Forest")

    meses = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    dias_semana = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


    month = st.slider('Mes', 0, 11)
    year = st.slider("Año", 2018, 2025)
    weekday = st.slider("Día de la semana", 0, 6)
    workingday = st.selectbox("Día laborable", [0, 1])
    holiday = st.selectbox("Día festivo", [0, 1])
    weathersit = st.slider("Clima", 1, 4)
    temp = st.slider("Temperatura", 0, 35)
    hum = st.slider("Humedad", 0, 100)
    windspeed = st.slider("Velocidad del viento", 0 , 35)

    if st.button("Predecir"):
        prediction = prediccion(month, year, weekday, workingday, holiday, weathersit, temp, hum, windspeed)
        st.success(f"La cantidad de bicicletas alquiladas estimada es: {int(prediction)}")

if __name__ == '__main__':
    main()