# Generated by Django 4.0.2 on 2022-02-26 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='rok',
            field=models.PositiveSmallIntegerField(default=2000, max_length=4),
        ),
        migrations.AlterField(
            model_name='film',
            name='tytul',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
