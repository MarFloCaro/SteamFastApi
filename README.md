<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**<span style="color:plum">Machine Learning Operations (MLOps)</span>**</h1>

<p align="center">
  <img src="/src/MLOPs-Purple.png" alt="MLOPs" />
</p>

### Este primer proyecto individual nos hará recorrer el ciclo de Machine Learning Operations, partiendo de un dataset de juegos de la plataforma Steam, hasta llegar a un modelo de Machine Learning predictivo.
<br>
<p style="text-align: right; color: violet; font-size: 1.2em; font-weight: bold;">by Maria Florencia Caro, Cohorte 13</p><br>

# <h1 align=center> **Intro** </h1>

El desafío planteado en para este proyecto consiste en desarrollar un proceso de MLOs que incluya etapas de Ingeniería de Datos con su correspondiente Extraction, Transform and Load (ETL), pasando al Machine Learning, con Exploratory Data Analysis (EDA), junto con la exploración y entrenamiento de modelos; finalizando con el deployment tanto del modelo como de los datos del proceso ETL.

# <h1 align=center> **Desarrollo del Proyecto**</h1>

## Ingeniería de Datos

En el rol de Data Engineer, encaramos el proceso de ETL. El detalle del proceso puede ser encontrado en [etl.ipynb](/entregables/etl.ipynb), con comentarios en Markdown paso a paso, pero algunos de los pasos destacados son (en orden, aunque algunos pasos se repiten luego de su primera aparición):

+ Importación delibrerías y lectura del archivo original.
+ Conversión a dataframe de pandas, ejecución de info() para una primera observación general.
+ Observación el formato de los datos en el dataset, a la vez que observamos el diccionario de datos provisto
+ Observación de filas sin datos útiles (vacióo, datos inespecíficos, duplicados)
+ Eliminación de columnas que no van a ser usadas en aplicaciones posteriores, tales como ID
+ Conversión de los tipos de datos asignados por defecto a tipos adecuados
+ Exploración de columnas con similitudes y sustitución de datos ausentes usando las similitudes.
+ Eliminación de columnas redundantes (columnas que aportan datos casi idénticos)
+ Sustitución de valores string por valores float or NAN donde sea posible, y re-asignación de tipo de datos de la/s columnas que lo permitan
+ Reemplazo de valores sin relación con la columna donde se encuentran por NA
+ Reinicio el index y guardo el dataset como archivo de parquet (elegido por almacenar data types y su bajo peso de archivo comparado con alternativas .json y .csv) para posterior uso de la aplicación FAST API, para sus primeras 6 funciones

# <h1 align=center> **Entregables**</h1>

## Aplicación de FAST API

La aplicación se encuentra disponible en [la siguiente ubicación](https://steamfastapi.onrender.com/)

## Video

El video demostrando el funcionamiento de la aplicación se encuentra en [este link]()

## Índice de Archivos del Repo

### Carpeta Entregables
+ [ETL Jupyter Notebook](/entregables/etl.ipynb)
+ [EDA Jupyter Notebook](/entregables/eda.ipynb)
+ [Experimentacion y Entrenamiento Jupyter Notebook](entregables/experimentacion_entrenamiento.ipynb)

### Raíz del Repo (archivos de la app)
+ [Archivo Main de la app FAST API](main.py)
+ [Archivo Pickle con el pre procesamiento del Modelo](preprocessing_steps.pkl)
+ [Requerimientos de la app FAST API](requirements.txt)
+ [Valor del RMSE del modelo elegido](rmse_model.txt)
+ [Dataset para las funciones de consulta de la app FAST API](steam_data_clean.parquet)
+ [Dataset para el modelo de predicción de la app FAST API](steam_data_model.parquet)
+ [Archivo Pickle con el modelo de Machine Learning](trained_model.pkl)

## Fuentes de datos

### El repositorio no contiene los datos originales provistos para el proyecto, los mismos pueden ser encontrados en las siguientes ubicaciones:

+ [Dataset](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj?usp=drive_link): Carpeta con el archivo de origen en formato .json (steam_games.json).
+ [Diccionario de datos](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit?usp=drive_link): Diccionario con algunas descripciones de las columnas disponibles en el dataset.
<br/>
