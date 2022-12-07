import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

app = Celery('main')
app.config_from_object('django.conf:settings',
                       namespace='CELERY')
app.autodiscover_tasks()


# celery notification tasks
app.conf.beat_schedule = {
    'send-notifications-every-6-hours':{
        'task': 'main.tasks.send_notification_email',
        'schedule': crontab(minute=0, hour='*/6,6-22')
        # 'schedule': crontab(minute='*/1')
    }
}