# Generated by Django 4.2 on 2023-06-14 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes_Organizer', '0002_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='email',
            field=models.CharField(default='', max_length=128),
        ),
    ]