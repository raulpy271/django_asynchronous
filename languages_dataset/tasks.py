from os import environ

from celery import shared_task
from pandas import read_csv

from .models import Language
from .utils import get_all_files_path, get_extension, get_delimiter


def save_language(language):
    fields = language.to_dict()
    Language(**fields).save()


def save_dataset(df):
    for index in df.index:
        language = df.loc[index]
        save_language(language)


@shared_task
def save_csv(path):
    delimiter = get_delimiter(path)
    df = read_csv(path, delimiter)
    save_dataset(df)


@shared_task
def save_excel(path):
    pass


@shared_task
def save_json(path):
    pass


@shared_task
def save_yml(path):
    pass


def select_parser(file_path):
    get_parser = {
        'csv': save_csv,
        'tsv': save_csv,
        'xlsx': save_excel,
        'json': save_json,
        'yml': save_yml,
        'yaml': save_yml,
        'default': save_csv}
    extension = get_extension(file_path)
    if not extension in get_parser.keys():
        extension = 'default'
    return get_parser[extension]


@shared_task
def read_files():
    data_path = environ.get('DATA_SOURCE_PATH', 'data_source/')
    files_path = get_all_files_path(data_path)
    for file_path in files_path:
        parser = select_parser(file_path)
        return parser.delay(file_path)


