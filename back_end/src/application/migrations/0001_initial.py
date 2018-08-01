# Generated by Django 2.0.7 on 2018-07-31 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=120)),
                ('last', models.CharField(max_length=120)),
                ('date_created', models.DateTimeField(default='')),
                ('expiration_date', models.DateTimeField(default='')),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
