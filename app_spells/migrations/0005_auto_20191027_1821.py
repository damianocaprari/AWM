# Generated by Django 2.1.4 on 2019-10-27 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_spells', '0004_auto_20191016_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spellca',
            name='owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='custom_attributes', to='app_spells.Spell'),
        ),
    ]
