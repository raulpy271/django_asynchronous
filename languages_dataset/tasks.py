from os import environ

from celery import shared_task
from pandas import read_csv

from .models import Language
from .utils import get_all_files_path


def save_language(language):
    filds = {
        'name': language['name'],
        'year': language['year'],
        'paradigm': language['paradigm'],
        'site': language['site']}
    Language(**filds).save()


@shared_task
def save_dataset(df):
    for language in df:
        save_language(language)


def save_csv(csv_path, **kargs):
    df = read_csv(csv_path, **kargs)
    save_dataset(df)


def save_excel(excel_path, **kargs):
    df = read_csv(excel_path, **kargs)
    save_dataset(df)



def select_parser(file_path):
    pass


@shared_task
def read_files():
    data_path = environ.get('DATA_SOURCE_PATH', 'data_source/')
    files_path = get_all_files_path(data_path)
    for file_path in files_path:
        #parser, kargs = select_parser(file_path)
        #parser.delay(file_path, **kargs)
        print('\n', file_path, '\n')


def save_example():
    df = [{
        'name': 'VIM Script', 
        'year': 10, 
        'paradigm': 'crazy', 
        'site': 'https'}]
    save_dataset(df)


