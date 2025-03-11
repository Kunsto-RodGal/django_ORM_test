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
    Product,
    Rating,
    Restaurant,
    Sale,
    Staff,
    StaffRestaurant,
)


def run():
    # enter code below

    comments = Comment.objects.all()
    for comment in comments:
        print(comment.content_object)
