# Generated by Django 3.2.5 on 2021-08-05 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_auto_20210805_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventomodel',
            name='comissao',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]