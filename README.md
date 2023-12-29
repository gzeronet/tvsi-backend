## Guide for TVSI Backand Server

I've done for this backend server tasks. Usage:

---

### 1. Build docker image

>> cd ./djapp

>> docker build -t tvsi-backend:IMAGE_VERSION .

### 2. Run container

>> docker run -it --rm --net host tvsi-backend:IMAGE_VERSION


### 3. Cronjob (deploy for linux vm only)

>> crontab -e

>> add line: 0 0 * * * cd /your-server-path/ && python manage.py load_data > /dev/null


### 4. Unit Test

>> python manage.py test

### 5. Requirements (✓: finished —: undo)

#### DB Schema Design

* Design tables to store data from TVMAZE: Schedule, Episode , Show, Episode guest cast information. ✓
* Design User table to store user information. ✓ (use django user)
* Upon server starts, it should init the db if not exists yet. ✓ (in runserver.sh)

#### Data Loading:

* A cron job constantly loading Schedule, Episode, Show and Episode guest cast data for US country on a daily basis. ✓
* On an initial start when no related data is found in the db, the cron job should start loading data within past seven days right away (Be careful with the rate limit on TVMAZE calls). ✓ (in runserver.sh)


#### API For Users:

* Log in/out and registery of users. ✓
* Provide API for users to Like/UnLike or Bookmark/UnBookmark the Episode. ✓
* Provide API to search and sort Episodes based on their properties, and number of Likes. ✓
* Provide API to search Bookmarked Episode with Episode guest cast information embedded. ✓

#### Other Requirements

* Unit tests ✓ (just add a simple unit test)
* Clear README.md to introduce how to run or build the project. ✓
* Clear code structure and comments in the code. ✓ (django rest framework style)
* Friendly error handling in case of API failure. ✓ 
* Gracefully handle HTTP 429 responses (from TVMaze): simply retry the request after a small pause instead of treating it as a permanent failure. ✓
* Writing a Dockerfile and Makefile/Bash script to build a Docker image for this website - it contains a server inside. ✓

#### Bonus Points
* Reusable components. ✓
* Provide a cache layer such as Redis. —
* Provide pagination abilities in search API. ✓
* Notification upon cronjob succeeded. Could be any form like WS notification, email sent via webhook. — (need redis pubsub for ws/sse)


### 6. Screenshots

