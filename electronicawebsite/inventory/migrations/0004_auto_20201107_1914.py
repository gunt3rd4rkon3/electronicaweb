# Generated by Django 3.1.2 on 2020-11-07 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0003_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default='some string', max_length=200),
        ),
        migrations.AddField(
            model_name='productinstance',
            name='available_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productinstance',
            name='sinnombre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]