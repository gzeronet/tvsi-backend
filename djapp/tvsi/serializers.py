from rest_framework import serializers
from .models import Episode, EpisodeGuestCast


class EmptySerializer(serializers.Serializer):
    pass


class EpisodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Episode
        fields = (
            'id',
            'url',
            'name',
            'season',
            'number',
            'episode_type',
            'airdate',
            'airstamp',
            'runtime',
            'rating',
            'image',
            'summary',
            'show',
            'number_of_likes',
        )
        read_only_fields = (
            'number_of_likes',
        )


class EpisodeGuestCastSerializer(serializers.ModelSerializer):

    class Meta:
        model = EpisodeGuestCast
        fields = (
            'id',
            'url',
            'name',
        )


class BookmarkedEpisodeSerializer(serializers.ModelSerializer):
    guestcasts = EpisodeGuestCastSerializer(many=True, read_only=True)

    class Meta:
        model = Episode
        fields = (
            'id',
            'url',
            'name',
            'season',
            'number',
            'episode_type',
            'airdate',
            'airstamp',
            'runtime',
            'rating',
            'image',
            'summary',
            'show',
            'guestcasts',
        )
