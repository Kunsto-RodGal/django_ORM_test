from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from core.models import Rating, Restaurant


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name', 'restaurant_type')


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('restaurant', 'user', 'rating',)
