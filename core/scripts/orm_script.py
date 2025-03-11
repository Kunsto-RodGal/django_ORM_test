import random
from pprint import pprint

from django.contrib.auth.models import User
from django.db import connection
from django.db.models import F, Q
from django.utils import timezone

from core.models import Rating, Restaurant, Sale, Staff, StaffRestaurant


def run():
    # enter code below

    print(Restaurant.objects.filter(capacity__isnull=True))

    pprint(connection.queries)
