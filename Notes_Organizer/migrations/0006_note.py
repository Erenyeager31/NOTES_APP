# Generated by Django 4.2 on 2023-06-15 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes_Organizer', '0005_delete_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('email', models.CharField(max_length=128)),
            ],
        ),
    ]