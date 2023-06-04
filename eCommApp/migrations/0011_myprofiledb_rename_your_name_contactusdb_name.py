# Generated by Django 4.2.1 on 2023-06-03 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCommApp', '0010_contactusdb_rename_myorder_myorderdb_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='myProfileDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=90)),
                ('Last_Name', models.CharField(max_length=90)),
                ('Gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('Email', models.EmailField(max_length=90)),
                ('phone', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='contactusdb',
            old_name='Your_Name',
            new_name='Name',
        ),
    ]