# Generated by Django 3.1.11 on 2021-10-27 00:17

from django.db import migrations
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0046_auto_20211020_0045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buyersguideproductcategory',
            options={'ordering': [django.db.models.expressions.OrderBy(django.db.models.expressions.F('parent__sort_order'), nulls_first=True), django.db.models.expressions.OrderBy(django.db.models.expressions.F('parent__name'), nulls_first=True), 'sort_order', 'name'], 'verbose_name': 'Buyers Guide Product Category', 'verbose_name_plural': 'Buyers Guide Product Categories'},
        ),
    ]
