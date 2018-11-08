import argparse # este módulo nos ayuda cuando vamos a crear un script
import logging # con este módulo le vamos imprimiendo en la consola al usuario lo que está pasando
logging.basicConfig(level=logging.INFO)
import hashlib
import nltk
from nltk.corpus import stopwords # los stopwords no nos añaden valor al análisis ulterior (la, los, nos, etc.)
from urllib.parse import urlparse

import pandas as pd


logger = logging.getLogger(__name__) # obtenemos una referencia a nuestro logger con nuestro nombre interno de python


def main(filename):
    logger.info('Starting cleaning process')

    df = _read_data(filename)
    newspaper_uid = _extract_newspaper_uid(filename) # vamos a extraer la primera palabra del filename
    df = _add_newspaper_uid_column(df, newspaper_uid) # vamos a añadir la columna newspaper_uid al DataFrame(df)
    df = _extract_host(df) # vamos a añadir a la columan host los host que capturemos de la columna url
    df = _fill_missing_titles(df) # vamos a llenar los titulos vacíos
    df = _generate_uids_for_rows(df) # vamos a convertir los índices en hashes
    df = _remove_new_lines_from_body(df) # vamos a remover los saltos de línea \n
    df = _tokenize_column(df, 'title') # creamos una columna tokenizada de los titles
    df = _tokenize_column(df, 'body') # creamos una columna tokenizada de los titles
    df = _remove_duplicate_entries(df, 'title') # eliminamos duplicados
    df = _drop_rows_with_missing_values(df)
    _save_data(df, filename)

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


def _fill_missing_titles(df):
    logger.info('Filling the empty titles')
    missing_titles_mask = df['title'].isna()

    missing_titles = (df[missing_titles_mask]['url']
        .str.extract(r'(?P<missing_titles>[^/]+)$')
        .applymap(lambda title: title.split('-'))
        .applymap(lambda title_word_list: ' '.join(title_word_list))
    )

    df.loc[missing_titles_mask, 'title'] = missing_titles.loc[:, 'missing_titles']

    return df


def _generate_uids_for_rows(df):
    logger.info('Adding hashes uids to the index')
    uids = (df
        .apply(lambda row: hashlib.md5(bytes(row['url'].encode())), axis=1)
        .apply(lambda hash_object: hash_object.hexdigest())
    )

    df['uid'] = uids

    return df.set_index('uid')


def _remove_new_lines_from_body(df):
    logger.info('Removing new lines from body')
    stripped_body = (df
        .apply(lambda row: row['body'], axis=1) # obtenemos la columna body del DataFrame
        .apply(lambda body: list(body)) # convertimos el body en una lista de letras
        .apply(lambda letters: list(map(lambda letter: letter.replace('\n', ''), letters))) # iteramos entre cada letra y cambiamos /n por ''. Convertimos el objeto map en objeto lista, envolviéndolo en list()
        .apply(lambda letters_list: ''.join(letters_list)) # vamos a unir de nuevo la lista
    )

    df['body'] = stripped_body
    return df


def _tokenize_column(df, column_name):
    logger.info(f'Calculating the number of unique tokens in {column_name}')
    stop_words = set(stopwords.words('spanish')) # seteamos los stopwords a español

    n_tokens = (df
        .dropna() # eliminamos los NaN en caso que aún los haya
        .apply(lambda row: nltk.word_tokenize(row[column_name]), axis=1) # tokenizamos nuestra columna
        .apply(lambda tokens: list(filter(lambda token: token.isalpha(), tokens))) # eliminamos todas las palabras que no sean alfanuméricas
        .apply(lambda tokens_list: list(map(lambda token: token.lower(), tokens_list))) # convertir tokens a lower_case para compararlas correctamente con stopwords
        .apply(lambda word_list: list(filter(lambda word: word not in stop_words, word_list))) # eliminar palabras dentro de stopwords
        .apply(lambda valid_word_list: len(valid_word_list)) # obtenemos cuántas palabras son
    )

    df['n_tokens_' + column_name] = n_tokens # concatenamos el nombre de la columna con n_tokens para que se aplique a ambas columnas (body y title)

    return df


def _remove_duplicate_entries(df, column_name):
    logger.info('Removing duplicate entries')
    df.drop_duplicates(subset=[column_name], keep='first', inplace=True)

    return df


def _drop_rows_with_missing_values(df):
    logger.info('Dropping rows with missing data')

    return df.dropna()


def _save_data(df, filename):
    clean_filename = f'clean_{filename}'
    logger.info(f'Saving file at: {clean_filename}')
    df.to_csv(clean_filename)


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