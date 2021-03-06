# Generated by Django 3.1.7 on 2021-03-16 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210317_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionitem',
            name='color',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='auctionitem',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='auctionitem',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.location'),
        ),
        migrations.AlterField(
            model_name='auctionitem',
            name='model',
            field=models.CharField(max_length=50),
        ),
    ]
