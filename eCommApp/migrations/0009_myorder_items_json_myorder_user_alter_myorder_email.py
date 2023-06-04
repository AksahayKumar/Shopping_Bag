# Generated by Django 4.2.1 on 2023-06-02 23:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eCommApp', '0008_remove_myorder_items_json_remove_myorder_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myorder',
            name='Items_Json',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='myorder',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='Email',
            field=models.CharField(max_length=90),
        ),
    ]