# Generated by Django 4.1.1 on 2022-11-16 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aeroport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomAir', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Liste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('compagnie', models.CharField(max_length=100)),
                ('prixTicket', models.FloatField()),
                ('numVol', models.IntegerField()),
                ('dateDepart', models.DateField()),
                ('air', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vol.aeroport')),
            ],
        ),
    ]