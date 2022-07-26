# Generated by Django 4.0.6 on 2022-07-24 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0004_remove_results_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league', models.CharField(max_length=50)),
                ('fixture', models.CharField(max_length=50)),
                ('home_win', models.IntegerField()),
                ('draw', models.IntegerField()),
                ('away_win', models.IntegerField()),
                ('home_form', models.IntegerField()),
                ('away_form', models.IntegerField()),
            ],
            options={
                'ordering': ['-home_win', '-away_win'],
            },
        ),
    ]
