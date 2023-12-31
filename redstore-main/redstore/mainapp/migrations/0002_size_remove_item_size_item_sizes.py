# Generated by Django 4.2.3 on 2023-08-01 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='size',
        ),
        migrations.AddField(
            model_name='item',
            name='sizes',
            field=models.ManyToManyField(blank=True, related_name='items', to='mainapp.size'),
        ),
    ]
