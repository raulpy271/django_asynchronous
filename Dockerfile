FROM python:3.8   

ENV DockerHOME=/djangoAsynchronous
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

WORKDIR $DockerHOME  
COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip  
RUN pip install -r /requirements.txt  

CMD python manage.py runserver 0.0.0.0:8000

