# Generated by Django 2.1.4 on 2019-10-16 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_spells', '0003_auto_20191015_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spelladditionalinfo',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/spell'),
        ),
    ]
