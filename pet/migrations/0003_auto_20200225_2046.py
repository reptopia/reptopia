# Generated by Django 3.0.2 on 2020-02-25 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0002_auto_20200225_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='bod',
            field=models.DateField(blank=True, null=True),
        ),
    ]
