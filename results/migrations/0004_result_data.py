# Generated by Django 2.0.1 on 2018-01-22 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_result_respondent_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
    ]