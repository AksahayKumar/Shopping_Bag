# Generated by Django 4.1.7 on 2023-04-25 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=50)),
                ('productCategory', models.CharField(default='', max_length=50)),
                ('productSubCategory', models.CharField(default='', max_length=50)),
                ('productPrice', models.IntegerField(default=0)),
                ('productDescription', models.CharField(max_length=500)),
                ('publishedDate', models.DateField()),
                ('productImage', models.ImageField(upload_to='images')),
            ],
        ),
    ]
