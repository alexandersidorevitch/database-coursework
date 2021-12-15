from datetime import date

from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
from rest_framework import serializers
from rest_framework.authtoken.models import Token

name_validator = RegexValidator(regex=r'^[\w\-\s]+$',
                                message='Not valid string for name')


def date_validator(value):
    if (date.today() - value).days // 365 > 200:
        raise serializers.ValidationError(f'You\'re more younger than {(date.today() - value).days // 365} years')


class Address(models.Model):
    street_name = models.CharField(max_length=255, validators=[name_validator])
    house_number = models.IntegerField()
    flat_number = models.IntegerField()
    level = models.IntegerField(blank=True)
    postcode = models.IntegerField(blank=True)

    def __str__(self):
        return f'Street: {self.street_name} House number: {self.house_number} Flat number: {self.flat_number}'


class Shop(models.Model):
    name = models.CharField(max_length=255, unique=True, validators=[name_validator])
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, validators=[name_validator])
    min_age = models.IntegerField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    fullname = models.CharField(max_length=255, validators=[name_validator])
    phone_regex = RegexValidator(
        regex=r'(?:\+375|80)\s?\(?\d\d\)?\s?\d\d(?:\d[\-\s]\d\d[\-\s]\d\d|[\-\s]\d\d[\-\s]\d\d\d|\d{5})',
        message="Your phone number isn't allowed")
    phone_number = models.CharField(max_length=18, validators=[phone_regex])
    birthdate = models.DateField(blank=True, validators=[date_validator])
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.fullname


class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.date


# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
