# Generated by Django 2.0 on 2018-01-12 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attributes', '0006_auto_20180112_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Option_Code', models.IntegerField()),
                ('Option_Label', models.CharField(max_length=200)),
                ('type', models.IntegerField()),
                ('Standard_variable_option', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='option',
            name='Attribute',
        ),
        migrations.RemoveField(
            model_name='option',
            name='connections',
        ),
        migrations.RenameModel(
            old_name='Attribute',
            new_name='Attributes',
        ),
        migrations.DeleteModel(
            name='Option',
        ),
        migrations.AddField(
            model_name='options',
            name='Attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attributes.Attributes'),
        ),
        migrations.AddField(
            model_name='options',
            name='connections',
            field=models.ManyToManyField(blank=True, related_name='_options_connections_+', to='attributes.Options'),
        ),
    ]
