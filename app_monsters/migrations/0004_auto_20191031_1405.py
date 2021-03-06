# Generated by Django 2.1.5 on 2019-10-31 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_monsters', '0003_auto_20191030_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='ability_cha',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='monster',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/monsters'),
        ),
    ]
