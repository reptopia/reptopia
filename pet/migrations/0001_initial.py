# Generated by Django 3.0.2 on 2020-02-25 01:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dict', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('bod', models.DateField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='pet/%Y/%m/%d')),
                ('desc', models.TextField(blank=True)),
                ('is_keeping', models.BooleanField(default=True)),
                ('gender', models.ForeignKey(limit_choices_to={'category': 'GT00000000'}, on_delete=django.db.models.deletion.CASCADE, related_name='gender', to='dict.Dictionary')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dict.AnimalDictionary')),
            ],
        ),
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prey_weight', models.IntegerField(blank=True, null=True)),
                ('prey_quantity', models.IntegerField(default=1)),
                ('prey_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prey_size', to='dict.Dictionary')),
                ('prey_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prey_type', to='dict.Dictionary')),
            ],
        ),
        migrations.CreateModel(
            name='Care',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('weight', models.IntegerField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='care/%Y/%m/%d')),
                ('desc', models.TextField(blank=True)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('feeding', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pet.Feeding')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet.Pet')),
                ('type', models.ForeignKey(limit_choices_to={'category': 'CT00000000'}, on_delete=django.db.models.deletion.CASCADE, related_name='care_type', to='dict.Dictionary')),
            ],
        ),
    ]
