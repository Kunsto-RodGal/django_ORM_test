import random
import time
from pprint import pprint

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import connection, transaction
from django.db.models import F, Q
from django.utils import timezone

from core.models import Product, Rating, Restaurant, Sale, Staff, StaffRestaurant


def run():
    # enter code below

    content_types = ContentType.objects.all()
    print(content_types)
