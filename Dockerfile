FROM python:3.8   

ENV DockerHOME=/djangoAsynchronous
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

WORKDIR $DockerHOME  

COPY requirements.txt /requirements.txt
COPY install-dep.sh /install-dep.sh

RUN bash /install-dep.sh

