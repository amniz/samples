# Generated by Django 2.2.4 on 2019-08-17 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FundooApp', '0002_fundoonotes_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundoonotes',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='fundoonotes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]