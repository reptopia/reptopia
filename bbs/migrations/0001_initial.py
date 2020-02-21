# Generated by Django 3.0.2 on 2020-02-21 06:50

import ckeditor_uploader.fields
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
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('board_status', models.ForeignKey(limit_choices_to={'category': 'BS00000000'}, on_delete=django.db.models.deletion.CASCADE, related_name='board_status', to='dict.Dictionary')),
                ('board_type', models.ForeignKey(limit_choices_to={'category': 'BT00000000'}, on_delete=django.db.models.deletion.CASCADE, related_name='board_type', to='dict.Dictionary')),
            ],
        ),
    ]
