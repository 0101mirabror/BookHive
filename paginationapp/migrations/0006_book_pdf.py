# Generated by Django 4.1.9 on 2023-07-06 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginationapp', '0005_remove_author_category_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pdf',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
