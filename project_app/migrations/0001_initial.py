# Generated by Django 4.2.5 on 2023-10-27 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobno', models.IntegerField(verbose_name=50)),
                ('email', models.CharField(max_length=50)),
                ('address1', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
    ]
