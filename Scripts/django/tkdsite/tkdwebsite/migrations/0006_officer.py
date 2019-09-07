# Generated by Django 2.2.4 on 2019-09-02 05:20

from django.db import migrations, models
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('tkdwebsite', '0005_instructor_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('Name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('image', models.ImageField(default='default.jpg', upload_to='officer_pics')),
                ('text', tinymce.models.HTMLField()),
                ('page_order', models.IntegerField(default=0)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
