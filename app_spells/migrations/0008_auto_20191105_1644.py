# Generated by Django 2.1.4 on 2019-11-05 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_spells', '0007_auto_20191105_1644'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='spell',
            unique_together={('name', 'version')},
        ),
    ]