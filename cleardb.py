from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Clear all tables in the database'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            # Disable foreign key checks and cascade delete
            cursor.execute("""
                DROP SCHEMA public CASCADE;
                CREATE SCHEMA public;
            """)
            self.stdout.write(self.style.SUCCESS('Successfully cleared database'))