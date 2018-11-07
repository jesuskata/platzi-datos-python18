import argparse # este módulo nos ayuda cuando vamos a crear un script
import logging # con este módulo le vamos imprimiendo en la consola al usuario lo que está pasando
logging.basicConfig(level=logging.INFO)
from urllib.parse import urlparse

import pandas as pd


logger = logging.getLogger(__name__) # obtenemos una referencia a nuestro logger con nuestro nombre interno de python


def main(filename):
    logger.info('Starting cleaning process')

    df = _read_data(filename)
    newspaper_uid = _extract_newspaper_uid(filename) # vamos a extraer la primera palabra del filename
    df = _add_newspaper_uid_column(df, newspaper_uid) # vamos a añadir la columna newspaper_uid al DataFrame(df)
    df = _extract_host(df)

    return df


def _read_data(filename):
    logger.info(f'Reading file {filename}')

    return pd.read_csv(filename) # como lo vimos en el jupyter notebooks, leemos el archivo csv


def _extract_newspaper_uid(filename):
    logger.info('Extracting newspaper uid')
    newspaper_uid = filename.split('_')[0] # vamos a tomar la primera parte del filename, si lo dividimos en guiones bajos

    logger.info(f'Newspaper uid detected: {newspaper_uid}')
    return newspaper_uid


def _add_newspaper_uid_column(df, newspaper_uid):
    logger.info(f'Filling newspaper_uid with {newspaper_uid}')
    df['newspaper_uid'] = newspaper_uid # Agregamos los datos de newspaper_uid a la nueva columna que se está agregando al df

    return df


def _extract_host(df):
    logger.info('Extracting host from url')
    df['host'] = df['url'].apply(lambda url: urlparse(url).netloc) # vamos a extraer solo el host de la columna url del df

    return df


if __name__ == '__main__':
    parser = argparse.ArgumentParser() # preguntamos al usuario cuál es el archivo (Dataset) que queremos trabajar
    parser.add_argument( # le añadimos un argumento: filename
        'filename',
        help='The path to the dirty data',
        type=str
    )

    args = parser.parse_args() # ahora parseamos los argumentos
    df = main(args.filename) # pasamos el argumento a la función main y lo pasamos a una variable para imprimirla en la consola
    print(df)