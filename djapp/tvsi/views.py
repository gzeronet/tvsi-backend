from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Episode
from .filters import EpisodeFilter
from .serializers import (
    EpisodeSerializer, EmptySerializer, BookmarkedEpisodeSerializer)


class EpisodeViewSet(mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    filterset_class = EpisodeFilter
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

    def get_queryset(self):
        return super().get_queryset().prefetch_related('user_liked')

    @action(detail=True, methods=['put'], serializer_class=EmptySerializer)
    def like(self, request, pk=None):
        """
        like episode api
        """
        instance = self.get_object()
        request.user.liked_episodes.add(instance)
        return Response({"message": f"liked {instance}"})

    @action(detail=True, methods=['put'], serializer_class=EmptySerializer)
    def unlike(self, request, pk=None):
        """
        unlike episode api
        """
        instance = self.get_object()
        request.user.liked_episodes.remove(instance)
        return Response({"message": f"unliked {instance}"})

    @action(detail=True, methods=['put'], serializer_class=EmptySerializer)
    def bookmark(self, request, pk=None):
        """
        bookmark episode api
        """
        instance = self.get_object()
        request.user.bookmarked_episodes.add(instance)
        return Response({"message": f"bookmarked {instance}"})

    @action(detail=True, methods=['put'], serializer_class=EmptySerializer)
    def unbookmark(self, request, pk=None):
        """
        unbookmark episode api
        """
        instance = self.get_object()
        request.user.bookmarked_episodes.remove(instance)
        return Response({"message": f"unbookmarked {instance}"})


class BookmarkedEpisodeViewSet(mixins.ListModelMixin,
                               viewsets.GenericViewSet):
    queryset = Episode.objects.all()
    serializer_class = BookmarkedEpisodeSerializer

    def get_queryset(self):
        return super().get_queryset().filter(
            user_bookmarked=self.request.user
        ).prefetch_related('guestcasts')
