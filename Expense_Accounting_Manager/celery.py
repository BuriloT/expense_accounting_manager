import os
from celery.schedules import crontab
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Expense_Accounting_Manager.settings')

app = Celery('Expense_Accounting_Manager')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.enable_utc = False

app.conf.beat_schedule = {
    'everyday_email': {
        'task': 'users.tasks.send_statistics',
        'schedule': crontab(minute=00, hour=7)
    }
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
