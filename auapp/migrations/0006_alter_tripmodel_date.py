# Generated by Django 3.2 on 2022-07-22 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auapp', '0005_alter_tripmodel_srno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripmodel',
            name='Date',
            field=models.DateField(verbose_name='Date(mm-dd-yyy)'),
        ),
    ]