# Generated by Django 5.0.4 on 2024-05-25 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_artikel_created_artikel_is_published_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artikel',
            options={'default_permissions': ('add', 'change', 'delete'), 'permissions': (('publish_artikel', 'can publish artikel'), ('edit_artikel', 'can edit artikel'))},
        ),
    ]