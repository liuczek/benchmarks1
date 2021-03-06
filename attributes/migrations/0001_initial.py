# Generated by Django 2.0 on 2018-01-12 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Attribute', models.IntegerField()),
                ('Attribute_Code', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Option_Code', models.IntegerField()),
                ('Option_Label', models.CharField(max_length=200)),
                ('Attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attributes.Attributes')),
            ],
        ),
    ]
