# Generated by Django 3.2.6 on 2021-08-21 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Designathon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('College', models.CharField(max_length=200)),
                ('name1', models.CharField(default=' ', max_length=20)),
                ('email1', models.EmailField(max_length=254)),
                ('phone1', models.BigIntegerField()),
                ('branch1', models.CharField(default=' ', max_length=50)),
                ('name2', models.CharField(default=' ', max_length=20)),
                ('email2', models.EmailField(max_length=254)),
                ('phone2', models.BigIntegerField()),
                ('branch2', models.CharField(default=' ', max_length=50)),
                ('name3', models.CharField(default=' ', max_length=20)),
                ('email3', models.EmailField(max_length=254)),
                ('phone3', models.BigIntegerField()),
                ('branch3', models.CharField(default=' ', max_length=50)),
                ('name4', models.CharField(default=' ', max_length=20)),
                ('email4', models.EmailField(max_length=254)),
                ('phone4', models.BigIntegerField()),
                ('branch4', models.CharField(default=' ', max_length=50)),
                ('id1', models.FileField(upload_to='Designathon/')),
                ('id2', models.FileField(blank=True, null=True, upload_to='Designathon/')),
                ('id3', models.FileField(blank=True, null=True, upload_to='Designathon/')),
                ('id4', models.FileField(blank=True, null=True, upload_to='Designathon/')),
            ],
        ),
    ]
