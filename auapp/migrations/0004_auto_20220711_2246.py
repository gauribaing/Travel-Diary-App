# Generated by Django 3.2 on 2022-07-11 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auapp', '0003_rename_rno_tripmodel_srno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tripmodel',
            old_name='date',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='tripmodel',
            old_name='dest',
            new_name='Destination',
        ),
        migrations.RenameField(
            model_name='tripmodel',
            old_name='ms',
            new_name='Pic',
        ),
        migrations.RenameField(
            model_name='tripmodel',
            old_name='desc',
            new_name='Text',
        ),
    ]
