from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Episode, Show


User = get_user_model()


class EpisodeTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="test-user")
        show = Show.objects.create(
            id=1,
            url="https://www.tvmaze.com/shows/15309/morning-joe",
            name="Morning Joe",
            show_type="News",
            language="English",
            genres=[],
            status="Running",
            runtime=240,
            average_runtime=186,
            premiered="2006-04-09",
            ended=None,
            official_site="https://www.nbc.com/morning-joe",
            schedule={
                "time": "06:00",
                "days": ["Monday"],
            },
            rating={"average": None},
            weight=82,
            network={
                "id": 201,
                "name": "MSNBC",
                "country": {
                    "name": "United States",
                    "code": "US",
                    "timezone": "America/New_York"
                }, "officialSite": None},
            web_channel=None,
            dvd_country=None,
            externals={
                "tvrage": None,
                "thetvdb": 282626,
                "imdb": "tt1170244"
            },
            image={},
            summary="test summary",
            updated=1703607576,
        )
        Episode.objects.create(
            id=1,
            name="test-episode",
            season=1,
            number=1,
            episode_type="test-type",
            airdate="2023-12-26",
            airtime="7:00",
            airstamp="2023-12-26T12:00:00+00:00",
            runtime=120,
            rating={},
            image={},
            summary="test summary",
            show=show,
        )

    def test_number_of_likes(self):
        user = User.objects.get(username="test-user")
        episode = Episode.objects.get(name="test-episode")
        user.liked_episodes.add(episode)
        self.assertEqual(episode.number_of_likes, 1)
