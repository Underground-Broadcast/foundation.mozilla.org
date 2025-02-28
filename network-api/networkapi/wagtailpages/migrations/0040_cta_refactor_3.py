# Generated by Django 3.1.11 on 2021-09-23 18:23

from django.db import migrations, models
import django.db.models.deletion

def print_progress(apps, schema_editor):
    print('Applying wagtailpages 0040')


def copy_petition_cta_to_cta(apps, schema_editor):
    CTA = apps.get_model("wagtailpages", "CTA")

    models = [
        apps.get_model("wagtailpages", "CampaignPage"),
        apps.get_model("wagtailpages", "BanneredCampaignPage"),
    ]

    for Model in models:
        for page in Model.objects.all():
            if page.petition_cta:
                page.cta = CTA.objects.get(
                    pk=page.petition_cta.pk,
                )
                page.save()

class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0039_cta_refactor_2'),
    ]

    operations = [
        migrations.RunPython(
            code=print_progress,
        ),
        migrations.AddField(
            model_name='banneredcampaignpage',
            name='cta',
            field=models.ForeignKey(blank=True, help_text='Choose an existing, or create a new, pettition form', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='banner_page_for_cta', to='wagtailpages.cta'),
        ),
        migrations.AddField(
            model_name='campaignpage',
            name='cta',
            field=models.ForeignKey(blank=True, help_text='Choose existing or create new sign-up form', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='campaign_page_for_cta', to='wagtailpages.cta'),
        ),
        migrations.RunPython(
            code=copy_petition_cta_to_cta
        )
    ]
