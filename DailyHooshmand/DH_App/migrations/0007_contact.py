# Generated by Django 3.2.4 on 2023-05-05 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DH_App', '0006_alter_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=158)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]