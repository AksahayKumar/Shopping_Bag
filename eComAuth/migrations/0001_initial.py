# Generated by Django 4.1.7 on 2023-03-25 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signupDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254, verbose_name='@gmail.com')),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
