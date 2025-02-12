from pprint import pprint

from django.contrib.auth.models import User
from django.db import connection
from django.utils import timezone

from core.models import Rating, Restaurant, Sale


def run():
    # enter code below

    restaurants = Restaurant.objects.all()
    pprint(restaurants)
    pprint(connection.queries)

    user, created = User.objects.get_or_create(username='admin')
