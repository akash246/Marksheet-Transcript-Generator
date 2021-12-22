# Generated by Django 4.0 on 2021-12-22 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RangeInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left', models.CharField(max_length=200, null=True)),
                ('right', models.CharField(max_length=200, null=True)),
                ('stamp', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('sign', models.ImageField(blank=True, null=True, upload_to='image/')),
            ],
        ),
    ]