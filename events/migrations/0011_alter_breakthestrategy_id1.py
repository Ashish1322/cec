# Generated by Django 3.2.6 on 2021-08-25 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_alter_breakthestrategy_id1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakthestrategy',
            name='id1',
            field=models.FileField(upload_to='BreakTheStrategy/'),
        ),
    ]
