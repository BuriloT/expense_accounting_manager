import datetime as dt

from django.utils import timezone as tz
from django.core.mail import send_mail

from Expense_Accounting_Manager.celery import app
from Expense_Accounting_Manager.settings import EMAIL_HOST_USER
from api.models import Transaction
from users.models import User


@app.task
def send_statistics():
    try:
        users = User.objects.all()
        for user in users:
            yesterday = dt.datetime.now(tz=tz.utc) - dt.timedelta(days=1)
            subject = 'Ежедневная статистика'
            transactions = Transaction.objects.filter(
                user=user, time__gt=yesterday
            )
            amount = sum(
                [transaction.amount for transaction in transactions]
            )
            message = (f'Ваш баланс: {user.balance}\n'
                       f'Новых транзакций за сутки: {transactions.count()}\n'
                       f'За сутки баланс изменился на: {amount}\n'
                       'Ваш менеджер учёта расходов :)')
            email_from = EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message, email_from, recipient_list)
    except Exception as e:
        print(e)
