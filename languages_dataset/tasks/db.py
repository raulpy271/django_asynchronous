import sqlite3


def get_connection():
    db_file = 'db.sqlite3'
    return sqlite3.connect(db_file)


def save_in_db(language):
    connect = get_connection()
    params = (
        language['name'], 
        language['year'], 
        language['paradigm'], 
        language['site'])
    query = (
        'INSERT INTO "languages_dataset_language" \
            (name, year, paradigm, site) \
            values (?, ?, ?, ?);')
    with connect:
        cursor = connect.cursor()
        cursor.execute(query, params)


def save_dataset(df):
    for language in df:
        save_in_db(language)


