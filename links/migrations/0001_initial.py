# Generated by Django 2.0.6 on 2018-06-25 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('url', models.CharField(max_length=2000, unique=True)),
                ('title', models.CharField(blank=True, max_length=2000)),
                ('selection', models.CharField(blank=True, max_length=2000)),
                ('folder', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='links', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created', '-id'),
            },
        ),
    ]
