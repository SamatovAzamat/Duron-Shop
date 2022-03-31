# Generated by Django 3.2.4 on 2021-06-26 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210626_1847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorymodel',
            old_name='created',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.categorymodel'),
            preserve_default=False,
        ),
    ]
