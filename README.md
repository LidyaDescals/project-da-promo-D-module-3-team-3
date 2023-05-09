Día 1 (04/05/2023):

 - Creamos repositorio en GitHub.
 - Creamos working agreements.
 - Creamos canal de comunicación.
 - Empezamos a definir el tablero kanban.

Día 2 (05/05/2023):

 - Terminamos el kanban.
 - Empezamos el EDA: 
    - Comprobamos tipo de columnas.
    - Cambiamos dteday a formato datetime.
    - Eliminamos las columnas 'yr', 'mnth' y 'season'.
    - Creamos la columna 'year', 'month' y 'day' con los datos extraídos mediante los métodos de datetime.
    - Sustituímos los valores de weekday por los nombres de los días mediante métodos de datetime. 
    - Comprobamos nulos y duplicados.
 - Decidimos crear archivo src.

Día 3 (08/05/2023):

   - Terminamos la categorización 
   - Realizamos un heatmap y en base a lo observado, eliminamos la columna de la sensación térmica, puesto que es prácticamente idéntica a la de temperatura.
   - Exploramos los outliers de la columna 'casual', la de los clientes no registrados.


 <!-- Para día 4:
 - Continuar EDA.
 - Seguir estudiando el heatmap.
 - Valorar si separar el dataset. Calcular el porcentaje de cnt que representan 'casual' y 'registered' para cada día. 
 - Empezar a incluir en el archivo src las variables/funciones que vayamos creando. -->

Día 4 (08/05/2023)
  - Continuamos explorando el dataframe:
      - Analizamos el heatmap
      - Hacemos un pairplot y un qqplot
   - Decidimos mantener el dataset completo por el momento, sin separarlo por clientes casuales vs. registrados.
   - Con el test de saphiro confirmamos que nuestra variable dependiente ('cnt'), no sigue una distribución normal, al igual que 'casual' y 'registered'.

Para día 5:
   - Normalizar la variable dependiente
   - Comprobar que se cumplen las asunciones para una regresión lineal:
      - Homocedasticidad
      - Independiencia
   - Realizar ANOVA