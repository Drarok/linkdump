import csv

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction

from ...models import Link


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        """Read in an instapaper export file. Columns: URL, Title, Selection, Folder
        """
        user = User.objects.get(username=options['username'])
        updated = created = 0
        pathname = options['file']
        with open(pathname, 'r', newline='') as f:
            reader = csv.DictReader(f)
            with transaction.atomic():
                for row in reader:
                    link, is_created = Link.objects.get_or_create(url=row['URL'], user=user)
                    if is_created:
                        created += 1
                    else:
                        updated += 1
                    [setattr(link, attr.lower(), value) for attr, value in row.items()]
                    link.save()
            print('Updated %d links, created %d.' % (updated, created))
