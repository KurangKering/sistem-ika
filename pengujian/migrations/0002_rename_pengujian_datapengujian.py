# Generated by Django 3.2.5 on 2021-07-17 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_uji', '0001_initial'),
        ('pengujian', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pengujian',
            new_name='DataPengujian',
        ),
    ]