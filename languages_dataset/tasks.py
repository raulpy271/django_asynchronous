from celery import shared_task
from pandas import read_csv


@shared_task
def save_dataset():
    print('\n\n --- Hello async --- \n\n')


def save_csv(csv_path, **kargs):
    df = read_csv(csv_path, **kargs)
    save_dataset(df)


def save_excel(excel_path, **kargs):
    df = read_csv(excel_path, **kargs)
    save_dataset(df)



def select_parser(file_path):
    pass


def read_files(data_path):
    files_path = []
    for file_path in files_path:
        parser, kargs = select_parser(file_path)
        parser.delay(file_path, **kargs)


def save_example():
    df = [{
        'name': 'VIM Script', 
        'year': 10, 
        'paradigm': 'crazy', 
        'site': 'https'}]
    save_dataset(df)


