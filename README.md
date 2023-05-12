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


Día 4 (09/05/2023):

 - Continuamos explorando el dataframe:
    - Analizamos el heatmap
    - Hacemos un pairplot y un qqplot
 - Decidimos mantener el dataset completo por el momento, sin separarlo por clientes casuales vs. registrados.
 - Con el test de saphiro confirmamos que nuestra variable dependiente ('cnt'), no sigue una distribución normal, al igual que 'casual' y 'registered'.

Día 5 (10/05/2023):

 - Hacemos pairplots comparando los clientes generales, registrados y casuales con las diferentes variables categóricas.
 - Seguimos comparando los datos y empezamos a ver diferente comportamiento entre los clientes registrados y los casuales.
 - Decidimos que probablemente haya que realizar un modelo predictivo diferente para cada segmento de clientes.

Día 6 (11/05/2023):

 - Convertimos nuestras variables categóricas a formato 'category'
 - Eliminamos columnas sobrantes
 - Guardamos los datos limpios en un .csv
 - Comprobamos si nustras variables dependientes cumplen con la asución de normalidad.
       - Nuestras variables no cumplen asunción de normalidad
       - Tratamos de normalizar la variable 'registered', no siendo posible - Concluimos que no podemos hacer una regresión lineal para
      ninguna de nuestras posibles variables dependientes.

Día 7 (12/05/2023):

 - Estandarizamos las variables predictivas numéricas. 
 - Intentamos empezar el encoding pero no conseguimos avanzar mucho porque los datos de pronto no tienen sentido.  


Para día 8:
   - Hacer sprint review. 
   - Intentar que los datos vuelvan a tener sentido.
   - Hacer encoding de las variables categoricas.
   - VISTO LO VISTO, HAY QUE INVESTIGAR PORQUE TODO ES MENTIRA.