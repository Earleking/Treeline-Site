# Generated by Django 2.0.5 on 2018-06-11 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Treeline_gg', '0012_bestpractices_games_plaed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bestpractices',
            old_name='games_plaed',
            new_name='games_played',
        ),
    ]
