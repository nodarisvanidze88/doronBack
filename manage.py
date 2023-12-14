#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management import call_command
from django.core.management.base import BaseCommand

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'doronapp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Run migrations
        call_command('makemigrations', 'tablecreator')
        call_command('migrate', 'tablecreator')

if __name__ == '__main__':
    main()
