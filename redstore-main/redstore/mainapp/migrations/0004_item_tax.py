# Generated by Django 4.2.3 on 2023-08-14 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_remove_item_sizes_item_size_delete_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='tax',
            field=models.IntegerField(default=50, max_length=20),
        ),
    ]
