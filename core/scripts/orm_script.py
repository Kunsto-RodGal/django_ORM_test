import random
import time
from pprint import pprint

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import connection, transaction
from django.db.models import F, Q
from django.utils import timezone

from core.models import (
    Comment,
    Event,
    InprogressTask,
    Product,
    Rating,
    Restaurant,
    Sale,
    Staff,
    StaffRestaurant,
    Task,
    TaskStatus,
)


def run():
    # enter code below

    for i in range(1, 6):
        Event.objects.create(
            name=f"Event {i}",
            start_date=timezone.now() - timezone.timedelta(days=i),
            end_date=timezone.now()
        )

    print(Event.objects.count())
