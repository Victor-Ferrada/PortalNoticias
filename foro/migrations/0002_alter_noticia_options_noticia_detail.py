# Generated by Django 4.1 on 2024-09-24 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='noticia',
            options={'verbose_name': 'New', 'verbose_name_plural': 'News'},
        ),
        migrations.AddField(
            model_name='noticia',
            name='detail',
            field=models.TextField(default='Sin información'),
            preserve_default=False,
        ),
    ]
