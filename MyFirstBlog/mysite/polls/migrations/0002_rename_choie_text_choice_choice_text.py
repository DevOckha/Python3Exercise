# Generated by Django 4.0 on 2021-12-15 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choie_text',
            new_name='choice_text',
        ),
    ]