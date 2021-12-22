# Generated by Django 4.0 on 2021-12-21 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marktsheet_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('negative', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('master_roll', models.FileField(blank=True, null=True, upload_to='file/')),
                ('response_csv', models.FileField(blank=True, null=True, upload_to='file/')),
            ],
        ),
    ]