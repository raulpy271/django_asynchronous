from celery import Celery
from pandas import read_csv


app = Celery('tasks.tasks')


@app.task
def save_dataset(df):
    pass


@app.task
def save_csv(csv_path, **kargs):
    df = read_csv(csv_path, **kargs)
    save_dataset(df)


@app.task
def save_excel(excel_path, **kargs):
    df = read_csv(excel_path, **kargs)
    save_dataset(df)



def select_parser(file_path):
    pass


@app.task
def read_files(data_path):
    files_path = []
    for file_path in files_path:
        parser, kargs = select_parser(file_path)
        parser.delay(file_path, **kargs)


