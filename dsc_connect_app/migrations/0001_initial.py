# Generated by Django 3.0.2 on 2020-02-05 11:33

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dsc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('0', 'draft'), ('1', 'published')], max_length=1)),
                ('lead', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=50)),
                ('quote', models.CharField(max_length=512)),
                ('domains', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=512), size=None)),
                ('gmail', models.EmailField(blank=True, max_length=254)),
                ('cover', models.ImageField(upload_to='images/')),
                ('city', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=300)),
                ('team_size', models.IntegerField()),
                ('established_on', models.DateField()),
                ('created_on', models.DateTimeField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('website', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('medium', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('youtube', models.URLField(blank=True)),
                ('behance', models.URLField(blank=True)),
                ('custom', models.URLField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
