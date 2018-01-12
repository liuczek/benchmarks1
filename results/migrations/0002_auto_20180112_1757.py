# Generated by Django 2.0 on 2018-01-12 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attributes', '0007_auto_20180112_1716'),
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='attribute',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='cur_param', to='attributes.Options'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='result',
            name='parametres',
            field=models.ManyToManyField(related_name='all_param', to='attributes.Options'),
        ),
    ]
