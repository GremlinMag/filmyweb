# Generated by Django 4.0.1 on 2022-03-06 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0003_film_imdb_rating_film_opis_film_plakat_film_premiera_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DodatkoweInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('czas_trwania', models.PositiveSmallIntegerField(default=0)),
                ('gatunek', models.PositiveSmallIntegerField(choices=[(0, 'Inne'), (3, 'Drama'), (2, 'Komedia'), (4, 'Sco-fi'), (1, 'Horror')], default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='film',
            name='plakat',
            field=models.ImageField(blank=True, null=True, upload_to='plakaty'),
        ),
        migrations.AddField(
            model_name='film',
            name='dodatkowe',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filmyweb.dodatkoweinfo'),
        ),
    ]