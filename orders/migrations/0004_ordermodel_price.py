# Generated by Django 3.2.4 on 2021-08-06 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_ordermodel_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
