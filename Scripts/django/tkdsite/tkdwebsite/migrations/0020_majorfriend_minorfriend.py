# Generated by Django 2.2.4 on 2019-09-02 11:53

from django.db import migrations, models
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('tkdwebsite', '0019_tournaments_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='majorfriend',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('friendtype', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='friend_pics')),
                ('text', tinymce.models.HTMLField()),
                ('date_contributed', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_contributed', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='minorfriend',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('contribution', models.CharField(max_length=100)),
                ('date_contributed', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_contributed', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
