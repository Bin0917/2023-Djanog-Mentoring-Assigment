# Generated by Django 4.2.5 on 2023-11-06 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writtenDate', models.DateField(auto_created=True)),
                ('reply', models.CharField(max_length=70)),
                ('content', models.CharField(max_length=70)),
            ],
        ),
    ]