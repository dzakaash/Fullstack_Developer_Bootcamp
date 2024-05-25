# Generated by Django 5.0.4 on 2024-05-10 09:58

import contact.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='judul',
            field=models.CharField(max_length=20, validators=[contact.validators.validate_judul]),
        ),
    ]