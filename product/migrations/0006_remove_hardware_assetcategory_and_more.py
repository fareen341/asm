# Generated by Django 4.0.5 on 2022-11-21 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
        ('product', '0005_alter_hardware_assetcategory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hardware',
            name='assetcategory',
        ),
        migrations.RemoveField(
            model_name='hardware',
            name='assettype',
        ),
        migrations.AddField(
            model_name='hardware',
            name='asset_type',
            field=models.CharField(blank=True, choices=[('IT Assets', 'IT Assets'), ('Non IT Assets', 'Non IT Assets')], max_length=50),
        ),
        migrations.AddField(
            model_name='hardware',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='master.category'),
        ),
    ]