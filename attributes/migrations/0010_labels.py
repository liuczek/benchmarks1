# Generated by Django 2.0.1 on 2018-01-16 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attributes', '0009_setting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Labels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.IntegerField()),
                ('Label', models.CharField(max_length=200)),
                ('Attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attributes.Options')),
            ],
        ),
    ]
