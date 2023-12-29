# Generated by Django 4.1 on 2023-12-29 01:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EpisodeGuestCast',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('url', models.URLField(null=True)),
                ('name', models.CharField(max_length=255)),
                ('country', models.JSONField(null=True)),
                ('birthday', models.DateField(null=True)),
                ('deathday', models.DateField(null=True)),
                ('gender', models.CharField(max_length=64, null=True)),
                ('image', models.JSONField(null=True)),
                ('updated', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('url', models.URLField(null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('show_type', models.CharField(max_length=64, null=True)),
                ('language', models.CharField(max_length=255, null=True)),
                ('genres', models.JSONField(default=list)),
                ('status', models.CharField(max_length=255, null=True)),
                ('runtime', models.PositiveIntegerField(null=True)),
                ('average_runtime', models.PositiveIntegerField(null=True)),
                ('premiered', models.DateField(null=True)),
                ('ended', models.DateField(null=True)),
                ('official_site', models.URLField(null=True)),
                ('schedule', models.JSONField(null=True)),
                ('rating', models.JSONField(null=True)),
                ('weight', models.PositiveIntegerField()),
                ('network', models.JSONField(null=True)),
                ('web_channel', models.JSONField(null=True)),
                ('dvd_country', models.JSONField(null=True)),
                ('externals', models.JSONField(null=True)),
                ('image', models.JSONField(null=True)),
                ('summary', models.TextField(null=True)),
                ('updated', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('url', models.URLField(null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('season', models.PositiveIntegerField(null=True)),
                ('number', models.PositiveIntegerField(null=True)),
                ('episode_type', models.CharField(max_length=64, null=True)),
                ('airdate', models.DateField(null=True)),
                ('airtime', models.TimeField(null=True)),
                ('airstamp', models.DateTimeField(null=True)),
                ('runtime', models.PositiveIntegerField(null=True)),
                ('rating', models.JSONField(null=True)),
                ('image', models.JSONField(null=True)),
                ('summary', models.TextField(null=True)),
                ('guestcasts', models.ManyToManyField(to='tvsi.episodeguestcast')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tvsi.show')),
                ('user_bookmarked', models.ManyToManyField(related_name='bookmarked_episodes', to=settings.AUTH_USER_MODEL)),
                ('user_liked', models.ManyToManyField(related_name='liked_episodes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tvsi.episode')),
            ],
            options={
                'unique_together': {('date', 'episode')},
            },
        ),
    ]
