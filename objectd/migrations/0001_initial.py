# Generated by Django 4.2.6 on 2023-10-13 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=510)),
                ('Description', models.TextField()),
                ('Ethnie', models.CharField(max_length=510)),
                ('Pays', models.CharField(max_length=510)),
                ('Materiaux', models.CharField(max_length=510)),
                ('Hauteur_cm', models.CharField(max_length=510)),
                ('Largeur_cm', models.CharField(max_length=510)),
                ('Poids', models.CharField(max_length=510)),
                ('Datation', models.CharField(max_length=510)),
                ('img', models.CharField(max_length=510)),
                ('img1', models.CharField(max_length=510)),
                ('img2', models.CharField(max_length=510)),
                ('img3', models.CharField(max_length=510)),
                ('img4', models.CharField(max_length=510)),
                ('img5', models.CharField(max_length=510)),
                ('img6', models.CharField(max_length=510)),
                ('img7', models.CharField(max_length=510)),
                ('img8', models.CharField(max_length=510)),
                ('img9', models.CharField(max_length=510)),
                ('img10', models.CharField(max_length=510)),
                ('img11', models.CharField(max_length=510)),
                ('img12', models.CharField(max_length=510)),
            ],
        ),
    ]
