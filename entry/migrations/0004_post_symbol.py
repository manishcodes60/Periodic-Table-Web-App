# Generated by Django 3.0.7 on 2020-07-01 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0003_auto_20200701_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='symbol',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]