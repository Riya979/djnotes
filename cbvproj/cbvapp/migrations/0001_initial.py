# Generated by Django 5.0.3 on 2024-03-27 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_no', models.IntegerField(max_length=20)),
                ('birth_date', models.DateField(max_length=20)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.IntegerField(max_length=50)),
                ('hire_date', models.DateField(max_length=50)),
            ],
        ),
    ]
