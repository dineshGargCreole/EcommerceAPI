# Generated by Django 3.2.4 on 2021-07-01 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210630_1910'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.AddField(
            model_name='product',
            name='tax',
            field=models.DecimalField(decimal_places=2, default=18, max_digits=4),
        ),
    ]
