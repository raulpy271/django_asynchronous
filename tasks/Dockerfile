FROM python:3.8   

ENV DockerHOME=/djangoAsynchronous
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

RUN mkdir -p $DockerHOME  
WORKDIR $DockerHOME  
COPY . $DockerHOME

RUN pip install --upgrade pip  
RUN pip install -r tasks/requirements.txt  

CMD celery \
    --broker amqp://guest:guest@rabbit:5672// \
    --app tasks.tasks worker \
    --loglevel=INFO

