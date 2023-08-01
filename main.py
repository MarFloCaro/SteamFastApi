from fastapi import FastAPI
import pandas as pd
from collections import Counter

app = FastAPI()

df = pd.read_parquet('steam_data_clean.parquet')
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')


def validar_entero(year):
    """ Validamos que el año provisto sea entero """

    try:
        return int(year)
    except:
        return False
    

def validar_anio(year):    
    """ Validamos que el año provisto esté dentro del dataset """

    min_year = int(df['release_date'].dt.year.min())
    max_year = int(df['release_date'].dt.year.max())

    if min_year > int(year) or int(year) > max_year:
        return min_year, max_year
    return False


@app.get('/')
def root():
    """ Mensaje de bienvenida """
    
    return {"message" : "Bienvenidos!"}


@app.get('/genero/{year}')
def genero(year:str): 
    """ Se ingresa un año en números enteros y devuelve una diccionario con los 5 géneros con más lanzamientos en ese año,
    en formato género: cantidad, en orden descendente por cantidad. En caso de no haber datos suficientes, retorna un mensaje de error.
    
    Ejemplo de retorno: {"Simulation":2,"Strategy":2,"Adventure":2,"Action":1,"Indie":1} """

    # Validamos que sea entero
    if not validar_entero(year):
        return {"error" : f"{year} no es un número entero válido"}
    
    #Convertimos a entero
    year = int(year)

    # Validamos el año esté dentro del rango
    if result := validar_anio(year):
        return {"error" : f"El año de lanzamiento no forma parte del dataset. Por favor pruebe valores entre {result[0]} y {result[1]}"}
    
    # Filtramos sólo las filas que corresponden al año
    genero_df = df[df['release_date'].dt.year == year]
    # Eliminamos los registros de género NaN
    genero_df.dropna(subset=['genres'], inplace=True)

    # Achatamos las listas de géneros de cada registro en una lista maestra
    lista_generos = [genre for sublista in genero_df['genres'] for genre in sublista]

    # Retornamos error si no hay género válidos
    if not lista_generos:
        return {"error": f"No se encontraron géneros válidos para el año {year}"}

    # Usamos la función Counter para contar las veces se repite cada género en la lista, formando un diccionario
    cuenta_genero = Counter(lista_generos)

    # Ordenamos el diccionario por valores en orden descendente
    sorted_genre_dict = dict(sorted(cuenta_genero.items(), key=lambda item: item[1], reverse=True))

    # Limitamos el diccionario a los top 5 usando slicing
    top_5_dict = {key: sorted_genre_dict[key] for key in list(sorted_genre_dict)[:5]}

    # Retornamos el diccionario limitado
    return top_5_dict


@app.get('/juegos/{year}')
def juegos(year:str):
    """Se ingresa un año en números enteros y devuelve un diccionario con los juegos lanzados en el año, usando el año como key
    y una lista con los nombres de los juegos como valor. En caso de no haber datos suficientes, retorna un mensaje de error.
    
    Ejemplo de retorno: {"1981":["Gallagher: Two Real","The Mystery of the Uurnog","Gallagher: Mad As Hell"]} """

    if not validar_entero(year):
        return {"error" : f"{year} no es un número entero válido"}
    
    year = int(year)
    
    if result := validar_anio(year):
        return {"error" : f"El año de lanzamiento no forma parte del dataset. Por favor pruebe valores entre {result[0]} y {result[1]}"}
    
    # Filtramos sólo las filas que corresponden al año
    juegos_df = df[df['release_date'].dt.year == year]

    # Listamos los juegos del año
    juegos_lista = juegos_df['app_name'].dropna().to_list()

    # Construímos el diccionario
    juegos_dict = {year: juegos_lista}

    # Retornamos el diccionario (o un error, si no hay lanzamientos registrados)
    return {"error": f"No se encontraron lanzamientos para el año {year}"} if not juegos_lista else juegos_dict


@app.get('/specs/{year}')
def specs(year:str):
    """Se ingresa un año en numeros entero y devuelve un diccionario con los 5 specs con más lanzamientos en ese año,
    en formato spec: cantidad, en orden descendente por cantidad. En caso de no haber datos suficientes, retorna un mensaje de error.
    
    Ejemplo de retorno: {"Single-player":45,"Multi-player":13,"Steam Cloud":10,"Steam Trading Cards":7,"Captions available":7} """

    if not validar_entero(year):
        return {"error" : f"{year} no es un número entero válido"}
    
    year = int(year)
    
    if result := validar_anio(year):
        return {"error" : f"El año de lanzamiento no forma parte del dataset. Por favor pruebe valores entre {result[0]} y {result[1]}"}
    
    # Filtramos sólo las filas que corresponden al año
    specs_df = df[df['release_date'].dt.year == year]
    # Eliminamos los registros de spec NaN
    specs_df.dropna(subset=['specs'], inplace=True)

    # Achatamos las listas de specs de cada registro en una lista maestra
    lista_specs = [spec for sublista in specs_df['specs'] for spec in sublista]

    # Retornamos error si no se encontraron specs válidos
    if not lista_specs:
        return {"error": f"No se encontraron specs válidos para el año {year}"} 

    # Usamos la función Counter para contar las veces se repite cada spec en la lista, formando un diccionario
    cuenta_specs = Counter(lista_specs)

    # Ordenamos el diccionario por valores en orden descendente
    sorted_specs_dict = dict(sorted(cuenta_specs.items(), key=lambda item: item[1], reverse=True))

    # Limitamos el diccionario a los top 5 usando slicing
    top_5_dict = {key: sorted_specs_dict[key] for key in list(sorted_specs_dict)[:5]}

    # Retornamos el diccionario limitado
    return top_5_dict


@app.get('/earlyaccess/{year}')
def earlyaccess(year:str):
    """ Se ingresa un año en números enteros y devuelve un diccionario con la cantidad juegos con early access lanzados en el año,
    usando el año como key y la cantidad de juegos como valor. En caso de no haber datos suficientes, retorna un mensaje de error.
    
    Ejemplo de retorno: {"2015":224} """

    if not validar_entero(year):
        return {"error" : f"{year} no es un número entero válido"}
    
    year = int(year)
    
    if result := validar_anio(year):
        return {"error" : f"El año de lanzamiento no forma parte del dataset. Por favor pruebe valores entre {result[0]} y {result[1]}"}
    
    # Filtramos sólo las filas que corresponden al año
    early_df = df[df['release_date'].dt.year == year]

    # Contamos los verdaderos
    early_total = int(early_df['early_access'].sum())

    # Retornamos la cantidad de juegos en early access para el año, o un error si no hay datos para ese año
    return {year: early_total} if early_total != 0 else {"error": f"No se encontraron datos de early access para el año {year}"}



@app.get('/sentiment/{year}')
def sentiment(year:str): 
    """ Se ingresa un año en numeros entero y devuelve un diccionario con la categroría de sentiment y la cantidad de registros para ese año,
    en formato sentiment: cantidad. En caso de no haber datos suficientes, retorna un mensaje de error.
    
    Ejemplo de retorno: {Mixed = 182, Very Positive = 120, Positive = 278} """    

    if not validar_entero(year):
        return {"error" : f"{year} no es un número entero válido"}
    
    year = int(year)
    
    if result := validar_anio(year):
        return {"error" : f"El año de lanzamiento no forma parte del dataset. Por favor pruebe valores entre {result[0]} y {result[1]}"}

    # Filtramos sólo las filas que corresponden al año
    sents_df = df[df['release_date'].dt.year == year]
    # Eliminamos los registros de sentiments NaN
    sents_df.dropna(subset=['sentiment'], inplace=True)

    # Listamos los sents
    lista_sents = sents_df['sentiment'].to_list()

    # Filtramos los datos de números de reviews que no indican sentimiento
    lista_sents = [sent for sent in lista_sents if "review" not in sent]

    # Retornamos error si no encontramos sents
    if not lista_sents:
        return {"error": f"No se encontraron sentiments válidos para el año {year}"}

    # Usamos la función Counter para contar las veces se repite cada sentimiento en la lista, formando un diccionario
    cuenta_sents = Counter(lista_sents)

    # Retornamos el diccionario de sentiments
    return cuenta_sents


@app.get('/metascore/{year}')    
def metascore(year:str):
    """Se ingresa un año en numeros entero y devuelve un diccionario con los 5 jeugos con mayor metascore en ese año,
    en formato juego: metascore, en orden descendente por cantidad. En caso de no haber datos suficientes, retorna un mensaje de error.
    
    Ejemplo de retorno: {"BioShock Infinite":94.0,"Deus Ex: Human Revolution - Director's Cut":91.0,"FEZ":91.0,"Brothers - A Tale of Two Sons":90.0,"Spelunky":90.0} """

    if not validar_entero(year):
        return {"error" : f"{year} no es un número entero válido"}
    
    year = int(year)
    
    if result := validar_anio(year):
        return {"error" : f"El año de lanzamiento no forma parte del dataset. Por favor pruebe valores entre {result[0]} y {result[1]}"}
    
    # Filtramos sólo las filas que corresponden al año
    meta_df = df[df['release_date'].dt.year == year]
    # Eliminamos los registros de score NaN
    meta_df.dropna(subset=['metascore'], inplace=True)

    # Creamos un dicionario usando 'app_name' como key y 'metascore' como valor
    metascores_dict = dict(zip(meta_df['app_name'], meta_df['metascore']))

    # Retornamos error si no se encontraron metascores válidos
    if not metascores_dict:
        return {"error": f"No se encontraron metascores válidos para el año {year}"}

    # Organizamos en orden descendiente
    metascores_dict_sorted = dict(sorted(metascores_dict.items(), key=lambda item: item[1], reverse=True))

    # Limitamos el diccionario al top 5
    top_5_dict = dict(list(metascores_dict_sorted.items())[:5])

    # Retornamos el diccionario limitado
    return top_5_dict

