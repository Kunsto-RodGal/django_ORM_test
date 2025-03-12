from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Q
from django.db.models.functions import Lower


def validate_restaurant_name_begins_with_a(value):
    if not value.startswith('a'):
        raise ValidationError('Restaurant name must begin with "a"')


class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        GREEK = 'GR', 'Greek'
        MEXICAN = 'MX', 'Mexican'
        FASTFOOD = 'FF', 'Fast Food'
        OTHER = 'OT', 'Other'

    name = models.CharField(max_length=100,
                            validators=[validate_restaurant_name_begins_with_a],
                            unique=True
                            )
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)])
    longitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])
    restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices)
    capacity = models.PositiveSmallIntegerField(null=True, blank=True)
    nickname = models.CharField(max_length=200, null=True, blank=True)
    comments = GenericRelation("Comment", related_query_name='restaurant')

    @property
    def restaurant_name(self):
        return self.nickname or self.name

    class Meta:
        ordering = [Lower('name'), 'date_opened']
        constraints = [
            models.CheckConstraint(
                name="valid_latitude",
                check=Q(latitude__gte=-90, latitude__lte=90),
                violation_error_message="Invalid Latitude"
            ),
            models.CheckConstraint(
                name="valid_longitude",
                check=Q(longitude__gte=-90, longitude__lte=90),
                violation_error_message="Invalid longitude"
            ),
            models.UniqueConstraint(
                Lower('name'),
                name='unique_name_constraint',
            )
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        print(self._state.adding)
        super().save(*args, **kwargs)


class Staff(models.Model):
    name = models.CharField(max_length=128)
    restaurants = models.ManyToManyField(Restaurant, through='StaffRestaurant')

    def __str__(self):
        return {self.name}


class StaffRestaurant(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    salary = models.FloatField(null=True)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comments = GenericRelation("Comment")

    def __str__(self):
        return f"Rating: {self.rating}"

    class Meta:
        constraints = [
            models.CheckConstraint(
                name='rating_value_valid',
                check=Q(rating__gte=1, rating__lte=5),
                violation_error_message="Rating invalid: must fall between 1 and 5."
            ),
            # Here is the method for constrains two fields and make them unique
            # models.UniqueConstraint(
            #     fields=['user', 'restaurant'],
            #     name='unique_rating_constraint'
            # )
        ]


class Sale(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.SET_NULL, null=True, related_name='sales')
    income = models.DecimalField(max_digits=8, decimal_places=2)
    expenditure = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    number_in_stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number_of_items = models.PositiveIntegerField()
    # user

    def __str__(self):
        return f"{self.number_of_items} x {self.product.name}"


class Comment(models.Model):
    text = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveSmallIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class TaskStatus(models.IntegerChoices):
    TODO = 1
    IN_PROGRESS = 2
    COMPLETED = 3


class Task(models.Model):
    name = models.CharField(max_length=100)
    ceated_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=TaskStatus.choices)

    def __str__(self):
        return self.name


class InprogressTask(Task):
    class Meta:
        proxy = True

    class Manager(models.Manager):
        def get_queryset(self) -> models.QuerySet:
            return super().get_queryset().filter(status=TaskStatus.IN_PROGRESS)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.status = TaskStatus.IN_PROGRESS
        super().save(*args, **kwargs)

    objects = Manager()
