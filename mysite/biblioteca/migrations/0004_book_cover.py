# Generated by Django 4.1.5 on 2023-02-18 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]