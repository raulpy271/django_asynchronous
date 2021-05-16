from os import environ

from celery import shared_task
from pandas import read_csv, read_excel, read_json, DataFrame
from yaml import load


from .models import Language
from .utils import (
    get_all_files_path,
    get_extension, 
    get_delimiter,
    catch_parser_error)


def save_language(language):
    fields = language.to_dict()
    Language(**fields).save()


def save_dataset(df):
    for index in df.index:
        language = df.loc[index]
        save_language(language)


@shared_task(name='parser_csv')
@catch_parser_error
def save_csv(path):
    delimiter = get_delimiter(path)
    df = read_csv(path, delimiter)
    save_dataset(df)


@shared_task(name='parser_excel')
@catch_parser_error
def save_excel(path):
    df = read_excel(path)
    save_dataset(df)


@shared_task(name='parser_json')
@catch_parser_error
def save_json(path):
    df = read_json(path)
    save_dataset(df)


@shared_task(name='parser_yml')
@catch_parser_error
def save_yml(path):
    with open(path) as yml_file:
        dict_of_yaml = load(yml_file)
        df = DataFrame(dict_of_yaml)
    save_dataset(df)


def select_parser(file_path):
    get_parser = {
        'csv': save_csv,
        'tsv': save_csv,
        'xlsx': save_excel,
        'xls': save_excel,
        'json': save_json,
        'yml': save_yml,
        'yaml': save_yml,
        'default': save_csv}
    extension = get_extension(file_path).lower()
    if not extension in get_parser.keys():
        extension = 'default'
    return get_parser[extension]


@shared_task(name='read_files')
def read_files():
    data_path = environ.get('DATA_SOURCE_PATH', 'data_source/')
    files_path = get_all_files_path(data_path)
    for file_path in files_path:
        parser = select_parser(file_path)
        parser.delay(file_path)


