# Generated by Django 4.1.9 on 2023-07-06 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginationapp', '0007_alter_book_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='books_number',
            field=models.IntegerField(default=0),
        ),
    ]