from celery import Celery

app = Celery('tasks.tasks')

@app.task
def add(x, y):
    return x + y

