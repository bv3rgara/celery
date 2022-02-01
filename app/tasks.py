from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time


@shared_task
def add(x, y):
    return x + y


@shared_task
def waitNSeconds(n):
    time.sleep(n)
