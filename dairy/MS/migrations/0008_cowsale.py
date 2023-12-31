# Generated by Django 4.2.3 on 2023-12-04 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MS', '0007_milksalereport'),
    ]

    operations = [
        migrations.CreateModel(
            name='CowSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=20, unique=True)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_contact', models.CharField(max_length=15)),
                ('customer_email', models.EmailField(max_length=254)),
                ('remarks', models.TextField()),
                ('cow_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MS.cowinfo')),
            ],
        ),
    ]
