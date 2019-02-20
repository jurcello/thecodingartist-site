# Generated by Django 2.1.5 on 2019-02-20 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('base', '0007_auto_20190220_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='formpage',
            name='search_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Search image'),
        ),
    ]