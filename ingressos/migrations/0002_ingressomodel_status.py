# Generated by Django 3.2.5 on 2021-08-06 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingressos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingressomodel',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
