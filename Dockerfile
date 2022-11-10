FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip3 install -r /app/requirements.txt --no-cache-dir

CMD ["gunicorn", "Expense_Accounting_Manager.wsgi:application", "--bind", "0:8000" ]