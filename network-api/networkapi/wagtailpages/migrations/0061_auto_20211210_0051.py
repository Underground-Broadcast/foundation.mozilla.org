# Generated by Django 3.1.11 on 2021-12-10 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0060_auto_20211201_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyersguideproductcategory',
            name='slug',
            field=models.SlugField(blank=True, help_text='A URL-friendly version of the category name. This is an auto-generated field.', max_length=100),
        ),
    ]
