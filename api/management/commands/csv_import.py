import csv

from django.core.management.base import BaseCommand

from ...models import Category


class Command(BaseCommand):
    help = 'import csv file to db'

    def handle(self, *args, **options):
        with open('data/categories.csv', encoding='utf-8') as file:
            file_reader = csv.reader(file)
            for row in file_reader:
                if len(row) > 1:
                    Category.objects.get_or_create(
                        name=row[0],
                        description=row[1],
                    )
                else:
                    Category.objects.get_or_create(
                        name=row[0]
                    )
