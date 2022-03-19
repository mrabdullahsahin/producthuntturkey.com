# Generated by Django 4.0 on 2022-03-19 14:37

from django.db import migrations, models
import django.db.models.deletion
import events.models
import parler.fields
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0009_alter_product_product_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(blank=True, max_length=350, null=True)),
                ('event_link', models.CharField(blank=True, max_length=500, null=True)),
                ('slug', models.SlugField(max_length=500, null=True, unique=True)),
                ('event_picture', models.ImageField(blank=True, default='default/producthuntturkey-logo.png', null=True, upload_to=events.models.Event.get_filepath)),
                ('event_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_avaliable', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('w', 'İnceleme Bekliyor'), ('d', 'Yayınlandı')], default='w', max_length=1)),
                ('event_city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.city')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='EventTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('event_description', models.TextField(blank=True, null=True)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='events.event')),
            ],
            options={
                'verbose_name': 'event Translation',
                'db_table': 'events_event_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases = (parler.models.TranslatableModel, models.Model),
        ),
    ]