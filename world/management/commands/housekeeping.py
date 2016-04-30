from django.core.management.base import NoArgsCommand, CommandError
from world.models import *
from django.utils import timezone

from datetime import date, timedelta, datetime

import logging

class Command(NoArgsCommand):
    args = 'None.'
    help = 'Performs housekeeping operations.'

    def handle_noargs(self, *args, **options):
        # delete SystemErrorLog records older than 31 days
        cutoff = timezone.now() - timedelta(days=31)
        records = SystemErrorLog.objects.filter(timestamp__lt=cutoff)
        records.delete()
        return