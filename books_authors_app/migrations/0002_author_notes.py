# Generated by Django 2.2 on 2021-05-19 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='Classics!'),
            preserve_default=False,
        ),
    ]
