from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Schedule(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    episode = models.ForeignKey('Episode', on_delete=models.PROTECT)

    class Meta:
        unique_together = ['date', 'episode']


class Episode(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.URLField(null=True)
    name = models.CharField(max_length=255, null=True)
    season = models.PositiveIntegerField(null=True)
    number = models.PositiveIntegerField(null=True)
    episode_type = models.CharField(max_length=64, null=True)
    airdate = models.DateField(null=True)
    airtime = models.TimeField(null=True)
    airstamp = models.DateTimeField(null=True)
    runtime = models.PositiveIntegerField(null=True)
    rating = models.JSONField(null=True)
    image = models.JSONField(null=True)
    summary = models.TextField(null=True)
    show = models.ForeignKey("Show", on_delete=models.PROTECT)
    guestcasts = models.ManyToManyField("EpisodeGuestCast")
    user_liked = models.ManyToManyField(
        User, related_name="liked_episodes")
    user_bookmarked = models.ManyToManyField(
        User, related_name="bookmarked_episodes")

    def __str__(self):
        return self.name

    @property
    def number_of_likes(self):
        return self.user_liked.count()


class Show(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.URLField(null=True)
    name = models.CharField(max_length=255, null=True)
    show_type = models.CharField(max_length=64, null=True)
    language = models.CharField(max_length=255, null=True)
    genres = models.JSONField(default=list)
    status = models.CharField(max_length=255, null=True)
    runtime = models.PositiveIntegerField(null=True)
    average_runtime = models.PositiveIntegerField(null=True)
    premiered = models.DateField(null=True)
    ended = models.DateField(null=True)
    official_site = models.URLField(null=True)
    schedule = models.JSONField(null=True)
    rating = models.JSONField(null=True)
    weight = models.PositiveIntegerField()
    network = models.JSONField(null=True)
    web_channel = models.JSONField(null=True)
    dvd_country = models.JSONField(null=True)
    externals = models.JSONField(null=True)
    image = models.JSONField(null=True)
    summary = models.TextField(null=True)
    updated = models.PositiveIntegerField(null=True)


class EpisodeGuestCast(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.URLField(null=True)
    name = models.CharField(max_length=255)
    country = models.JSONField(null=True)
    birthday = models.DateField(null=True)
    deathday = models.DateField(null=True)
    gender = models.CharField(max_length=64, null=True)
    image = models.JSONField(null=True)
    updated = models.IntegerField(null=True)

    def __str__(self):
        return self.name
