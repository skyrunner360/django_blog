# Generated by Django 3.0.7 on 2020-06-16 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('category', models.CharField(max_length=13)),
                ('author', models.CharField(max_length=100)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
