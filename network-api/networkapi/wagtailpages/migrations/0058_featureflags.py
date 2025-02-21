# Generated by Django 3.1.11 on 2021-11-22 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailpages', '0057_youtuberegretsreporterextensionpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureFlags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activate_donate_banner', models.BooleanField(default=False, help_text='This will show our donation banner at the top of all foundation pages, when checked', verbose_name='Activate the donation banner')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
