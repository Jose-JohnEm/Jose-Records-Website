# Generated by Django 3.2.6 on 2021-08-09 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('label', '0006_alter_prodtype_example'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prodtype',
            old_name='example',
            new_name='exemple',
        ),
    ]
