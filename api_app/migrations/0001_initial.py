# Generated by Django 4.2.6 on 2023-10-18 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppleCeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('slug', models.CharField(max_length=256)),
                ('first_year_active', models.IntegerField(null=True)),
            ],
        ),
    ]
