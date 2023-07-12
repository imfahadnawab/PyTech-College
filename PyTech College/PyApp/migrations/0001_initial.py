# Generated by Django 4.2.2 on 2023-07-10 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('fullname', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]