# Generated by Django 3.2.9 on 2021-12-07 22:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Not valid string for name', regex='^[A-z-\\s]+$')])),
                ('house_number', models.IntegerField()),
                ('flat_number', models.IntegerField()),
                ('level', models.IntegerField(blank=True)),
                ('postcode', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Not valid string for name', regex='^[A-z-\\s]+$')])),
                ('min_age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Not valid string for name', regex='^[A-z-\\s]+$')])),
                ('phone_number', models.CharField(max_length=18, validators=[django.core.validators.RegexValidator(message="Your phone number isn't allowed", regex='(?:\\+375|80)\\s?\\(?\\d\\d\\)?\\s?\\d\\d(?:\\d[\\-\\s]\\d\\d[\\-\\s]\\d\\d|[\\-\\s]\\d\\d[\\-\\s]\\d\\d\\d|\\d{5})')])),
                ('birthdate', models.DateField(blank=True, validators=[product.models.date_validator])),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.address')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(message='Not valid string for name', regex='^[A-z-\\s]+$')])),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.address')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.customer')),
                ('products', models.ManyToManyField(to='product.Product')),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.shop')),
            ],
        ),
    ]
