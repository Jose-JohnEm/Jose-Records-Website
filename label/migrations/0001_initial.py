# Generated by Django 3.2.6 on 2021-08-06 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('labeled', models.BooleanField()),
                ('picture', models.ImageField(upload_to='')),
                ('text', models.TextField(max_length=5000)),
            ],
        ),
    ]
