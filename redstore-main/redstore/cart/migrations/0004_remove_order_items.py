# Generated by Django 4.2.4 on 2023-09-04 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_order_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
    ]