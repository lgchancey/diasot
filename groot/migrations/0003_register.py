# Generated by Django 4.0.5 on 2022-06-17 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groot', '0002_rename_publications_publication'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
