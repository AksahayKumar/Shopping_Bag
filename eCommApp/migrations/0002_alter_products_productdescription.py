# Generated by Django 4.1.7 on 2023-04-26 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCommApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='productDescription',
            field=models.TextField(),
        ),
    ]
