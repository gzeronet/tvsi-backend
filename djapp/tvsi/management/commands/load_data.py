from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone
from requests.exceptions import HTTPError
from tvsi.models import Schedule, Episode, Show, EpisodeGuestCast
from datetime import timedelta
from time import sleep

import requests
import logging


RETRY_STATUS_CODE = 429

RETRY_INTERVAL = 3

TIMEOUT = 20

logger = logging.getLogger(__package__)


class Command(BaseCommand):
    help = "Load data from tvmaze api"

    def add_arguments(self, parser):
        parser.add_argument(
            '--past-seven-days',
            dest='past_seven_days',
            action='store_true',
            help='loading data within past seven days')

    def handle(self, *args, **options):
        past_days = 7 if options['past_seven_days'] else 1
        self.load_episodes(past_days)

    def load_guestcast(self, episode_id):
        """
        load episode guestcast with id
        """
        logger.info(f"start loading episode {episode_id} guestcasts")

        episode = Episode.objects.get(id=episode_id)
        json_response = []

        while True:
            try:
                rq = requests.get(
                    settings.GUESTCAST_ENDPOINT.format(episode.id),
                    timeout=TIMEOUT,
                    headers={
                        'content-type': 'application/json',
                    })
                rq.raise_for_status()
            except HTTPError as exc:
                if rq.status_code == RETRY_STATUS_CODE:
                    logger.warning(
                        f"busy on loading guestcast for {episode}: {exc}"
                    )
                    sleep(RETRY_INTERVAL)
                    continue
                logger.error(
                    f"failure on loading guestcast of episode {episode}: {exc}"
                )
                return
            except Exception as exc:
                logger.error(
                    f"failure on loading guestcast of episode {episode}: {exc}"
                )
                return

            else:
                logger.info(
                    f"success on loading guestcast of episodes {episode}")
                json_response = rq.json()
                break

        for guestcast_dict in json_response:
            person_dict = guestcast_dict["person"]
            guestcast, created = EpisodeGuestCast.objects.get_or_create(
                id=person_dict['id'], defaults={
                    "url": person_dict["url"],
                    "name": person_dict["name"],
                    "country": person_dict["country"],
                    "birthday": person_dict["birthday"],
                    "deathday": person_dict["deathday"],
                    "gender": person_dict["gender"],
                    "image": person_dict["image"],
                    "updated": person_dict["updated"],
                })
            episode.guestcasts.add(guestcast)

        logger.info(f"finished loading episode {episode_id} guestcasts")

    def load_episodes(self, past_days):
        today = timezone.localdate()
        for i in range(past_days):
            date = today - timedelta(i)
            logger.info(f"start loading episodes in {date}")
            json_response = []
            while True:
                try:
                    rq = requests.get(
                        settings.SCHEDULE_ENDPOINT,
                        timeout=TIMEOUT,
                        params={
                            'country': 'US',
                            'date': date.strftime("%Y-%m-%d")
                        },
                        headers={
                            'content-type': 'application/json',
                        })
                    rq.raise_for_status()
                except HTTPError as exc:
                    if rq.status_code == RETRY_STATUS_CODE:
                        logger.warning(
                            f"busy on loading schedule {date}: {exc}")
                        sleep(RETRY_INTERVAL)
                        continue
                    logger.error(f"failure on loading schedule {date}: {exc}")
                    return
                except Exception as exc:
                    logger.error(
                        f"failure on loading schedule {date}: {exc}"
                    )
                    return

                else:
                    logger.info(f"success on loading schedule {date}")
                    json_response = rq.json()
                    break

            for episode_dict in json_response:
                show_dict = episode_dict['show']
                Show.objects.get_or_create(
                    id=show_dict['id'], defaults={
                        'url': show_dict['url'],
                        'name': show_dict['name'],
                        'show_type': show_dict['type'],
                        'language': show_dict['language'],
                        'genres': show_dict['genres'],
                        'status': show_dict['status'],
                        'runtime': show_dict['runtime'],
                        'average_runtime': show_dict['averageRuntime'],
                        'premiered': show_dict['premiered'],
                        'ended': show_dict['ended'],
                        'official_site': show_dict['officialSite'],
                        'schedule': show_dict['schedule'],
                        'rating': show_dict['rating'],
                        'weight': show_dict['weight'],
                        'network': show_dict['network'],
                        'web_channel': show_dict['webChannel'],
                        'dvd_country': show_dict['dvdCountry'],
                        'externals': show_dict['externals'],
                        'image': show_dict['image'],
                        'summary': show_dict['summary'],
                        'updated': show_dict['updated'],
                    })

                Episode.objects.get_or_create(
                    id=episode_dict['id'], defaults={
                        'url': episode_dict['url'],
                        'name': episode_dict['name'],
                        'season': episode_dict['season'],
                        'number': episode_dict['number'],
                        'episode_type': episode_dict['type'],
                        'airdate': episode_dict['airdate'],
                        'airtime': episode_dict['airtime'],
                        'airstamp': episode_dict['airstamp'],
                        'runtime': episode_dict['runtime'],
                        'rating': episode_dict['rating'],
                        'image': episode_dict['image'],
                        'summary': episode_dict['summary'],
                        'show_id': show_dict['id'],
                    })

                Schedule.objects.get_or_create(
                    date=date,
                    episode_id=episode_dict['id']
                )
                self.load_guestcast(episode_dict['id'])

            logger.info(f"finished loading episodes in {date}")
