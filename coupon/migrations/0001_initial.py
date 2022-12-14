# Generated by Django 4.0.6 on 2022-08-15 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15, unique=True)),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('discount', models.IntegerField()),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Coupon Code',
            },
        ),
    ]
