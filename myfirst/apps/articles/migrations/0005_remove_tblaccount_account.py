# Generated by Django 4.1.4 on 2022-12-18 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_tblaccount_account_alter_tblaccount_born_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tblaccount',
            name='account',
        ),
    ]
