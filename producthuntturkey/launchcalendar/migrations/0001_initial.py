# Generated by Django 4.0 on 2022-06-28 15:35

from django.db import migrations, models
import django.db.models.deletion
import launchcalendar.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0009_alter_product_product_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaunchCalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField(max_length=250, null=True, unique=True)),
                ('product_about_tr', models.TextField(blank=True, null=True)),
                ('product_about_en', models.TextField(blank=True, null=True)),
                ('product_twitter', models.CharField(blank=True, max_length=250, null=True)),
                ('product_owner_twitter', models.CharField(blank=True, max_length=250, null=True)),
                ('product_ph_link', models.CharField(blank=True, max_length=250, null=True)),
                ('product_website', models.CharField(blank=True, max_length=250, null=True)),
                ('product_launch_date', models.DateField(blank=True, null=True)),
                ('product_picture', models.ImageField(blank=True, default='default/producthuntturkey-logo.png', null=True, upload_to=launchcalendar.models.LaunchCalendar.get_filepath)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('w', 'İnceleme Bekliyor'), ('p', 'Product Tablosuna Eklendi'), ('d', 'Yayınlama')], default='w', max_length=1)),
                ('product_city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.city')),
                ('product_team_size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.teamsize')),
            ],
        ),
    ]