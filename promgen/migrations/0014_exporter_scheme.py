# Generated by Django 2.2.10 on 2020-02-18 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promgen', '0013_validation_fix'),
    ]

    operations = [
        migrations.AddField(
            model_name='exporter',
            name='scheme',
            field=models.CharField(choices=[('http', 'http'), ('https', 'https')], default='http', help_text='Scrape exporter over http or https', max_length=5),
        ),
        migrations.AlterField(
            model_name='exporter',
            name='job',
            field=models.CharField(help_text='Exporter name. Example node, jmx, app', max_length=128),
        ),
        migrations.AlterField(
            model_name='exporter',
            name='path',
            field=models.CharField(blank=True, help_text='Exporter path. Defaults to /metrics', max_length=128),
        ),
        migrations.AlterField(
            model_name='exporter',
            name='port',
            field=models.IntegerField(help_text='Port Exporter is running on'),
        ),
    ]
