import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')


app =Celery('core')

app.config_from_object('django.conf:settings',namespace='CELERY')

app.conf.beat_schedule ={
    'scrape_result':{
        'task':'scrape.tasks.ScrapeResult',
        'schedule': 600.0
    },
    
    'scrape_result2':{
        'task':'scrape.tasks.ScrapeResult2',
        'schedule': 600.0
    },
    
     'scrape_result3':{
        'task':'scrape.tasks.ScrapeResult3',
        'schedule': 600.0
    },
    
     'scrape_result4':{
        'task':'scrape.tasks.ScrapeResult4',
        'schedule': 600.0
    }
}

app.autodiscover_tasks()
