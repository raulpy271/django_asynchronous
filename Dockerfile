FROM python:3.8   

ENV DockerHOME=/djangoAsynchronous
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

RUN mkdir -p $DockerHOME  
WORKDIR $DockerHOME  
COPY . $DockerHOME

RUN pip install --upgrade pip  
RUN pip install -r requirements.txt  

EXPOSE 8000  
CMD python manage.py runserver 0.0.0.0:8000

