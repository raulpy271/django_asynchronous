FROM python:3.8

ENV DockerHOME=/djangoAsynchronous
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR $DockerHOME  
COPY tasks/requirements.txt /requirements-tasks.txt

RUN pip install --upgrade pip  
RUN pip install -r /requirements-tasks.txt  

CMD celery \
    --broker amqp://guest:guest@rabbit:5672// \
    --app tasks.tasks worker \
    --loglevel=INFO

