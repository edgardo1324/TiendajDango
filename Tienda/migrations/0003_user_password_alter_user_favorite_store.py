# Generated by Django 4.2.1 on 2023-05-10 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Password',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tienda.store'),
        ),
        migrations.AlterField(
            model_name='user',
            name='favorite_store',
            field=models.CharField(max_length=255),
        ),
    ]
