# Generated by Django 3.2.6 on 2021-10-30 18:59

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 18, 59, 10, 716928), editable=False),
        ),
    ]