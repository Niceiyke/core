# Generated by Django 4.0.6 on 2022-07-24 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0006_prediction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
