# Generated by Django 3.1.11 on 2021-09-24 01:39

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0036_auto_20210917_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpage',
            name='tips_to_protect_yourself',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
