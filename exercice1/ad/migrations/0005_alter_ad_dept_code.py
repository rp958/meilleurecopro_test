# Generated by Django 5.2.1 on 2025-06-02 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ad", "0004_alter_ad_dept_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ad",
            name="dept_code",
            field=models.CharField(null=True),
        ),
    ]
