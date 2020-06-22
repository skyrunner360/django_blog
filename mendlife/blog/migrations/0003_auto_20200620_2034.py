# Generated by Django 3.0.7 on 2020-06-20 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('category', models.CharField(max_length=13)),
                ('author', models.CharField(max_length=100)),
                ('slug', models.CharField(default=' ', max_length=150)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default=' ', upload_to=''),
        ),
    ]
