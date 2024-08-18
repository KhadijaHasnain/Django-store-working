# Generated by Django 2.2.1 on 2019-06-17 08:26

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
            name='Store',
            fields=[
                ('name', models.CharField(max_length=30, verbose_name='Store name')),
                ('capacity', models.IntegerField(default=0, verbose_name='Capacity')),
                ('number_of_items', models.IntegerField(default=0)),
                ('store_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Manager', to=settings.AUTH_USER_MODEL)),
                ('store_users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]