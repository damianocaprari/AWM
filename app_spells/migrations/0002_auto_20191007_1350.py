# Generated by Django 2.1.4 on 2019-10-07 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_spells', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='spell',
            options={'ordering': ['level', 'name']},
        ),
        migrations.AlterModelOptions(
            name='spelladditionalinfo',
            options={},
        ),
        migrations.AlterModelOptions(
            name='spellca',
            options={},
        ),
        migrations.AlterModelOptions(
            name='spelltag',
            options={},
        ),
    ]
