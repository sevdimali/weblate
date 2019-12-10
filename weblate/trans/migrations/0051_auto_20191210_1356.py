# Generated by Django 2.2.5 on 2019-12-10 13:56

from django.db import migrations, models

from weblate.utils.licenses import get_license_choices


class Migration(migrations.Migration):

    dependencies = [("trans", "0050_licenses")]

    operations = [
        migrations.RemoveField(model_name="component", name="license_url"),
        migrations.AlterField(
            model_name="component",
            name="license",
            field=models.CharField(
                blank=True,
                choices=get_license_choices(),
                default="",
                max_length=150,
                verbose_name="Translation license",
            ),
        ),
    ]
