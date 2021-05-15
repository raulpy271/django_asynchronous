from os import environ

from celery import Celery


environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_asynchronous.settings')


app = Celery('django_asynchronous')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


