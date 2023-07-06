# Generated by Django 4.1.9 on 2023-07-02 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paginationapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('life', models.TextField()),
                ('image', models.ImageField(upload_to='author_images')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paginationapp.author'),
        ),
    ]
