# Generated by Django 4.0 on 2021-12-13 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='ürün ismi')),
                ('content', models.TextField(max_length=500, verbose_name='ürün açıklaması')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('stock_count', models.PositiveSmallIntegerField(verbose_name='stok_adedi')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ürün fiyatı')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'db_table': 'urunler',
            },
        ),
    ]