# Generated by Django 3.0.2 on 2020-02-08 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('value', models.CharField(default='', max_length=100)),
                ('display_order', models.IntegerField(default=0)),
                ('is_usable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalDictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=100)),
                ('common_name', models.CharField(max_length=100)),
                ('common_name_kor', models.CharField(max_length=100)),
                ('cites_appendices', models.ForeignKey(blank=True, limit_choices_to={'category': 'CA00000000'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cites_appendices', to='dict.Dictionary')),
                ('class_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='class_name', to='dict.Dictionary')),
                ('eating', models.ForeignKey(blank=True, limit_choices_to={'category': 'PT00000000'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eating', to='dict.Dictionary')),
                ('family', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='family', to='dict.Dictionary')),
                ('genus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='genus', to='dict.Dictionary')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='dict.Dictionary')),
            ],
        ),
    ]
