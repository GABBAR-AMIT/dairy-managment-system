# Generated by Django 4.2.3 on 2023-12-04 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MS', '0003_vaccinemonitoring'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedMonitoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('remarks', models.TextField()),
                ('food_item', models.CharField(max_length=50)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('feeding_time', models.TimeField()),
                ('cow_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MS.cowinfo')),
            ],
        ),
    ]
