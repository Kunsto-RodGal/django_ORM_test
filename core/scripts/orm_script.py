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

    # in_progress = Task.objects.filter(status=TaskStatus.IN_PROGRESS)
    in_progress = InprogressTask.objects.all()
    print(in_progress)
