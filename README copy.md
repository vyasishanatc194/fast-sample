# Padelmates - Backend

Padelmates Multipurpose API and Codebase

## Requirements

Python 3.8

```
fastapi==0.89.1
firebase==3.0.1
firebase-admin==6.0.1
pymongo==4.3.3
Pyrebase4==4.6.0
starlette==0.22.0
uvicorn==0.20.0
```

## Instructions for running codebase.

```
1. conda create -n padel python=3.8
2. conda activate padel
3. pip install -r requirements.txt
4. pip install -r requirements_dev.txt
5. python -m uvicorn main:app --reload
```

## Instructions for running codebase in aws ubuntu

```
1. Install Miniconda
2. conda create -n padel python=3.8
3. sudo apt install tmux
4. tmux
5. conda activate padel
6. pip install -r requirements.txt
7. pip install -r requirements_dev.txt
8. python -m uvicorn main:app --reload


9. Close terminal
10. Open a terminal
11. tmux ls
12. tmux attach -t 0
13. tmux detach
14. tmux kill-session -t 5
```
For changing nginx config: https://lcalcagni.medium.com/deploy-your-fastapi-to-aws-ec2-using-nginx-aa8aa0d85ec7

## Instructions for running on docker.

```
1. docker build . -t fastapi_padelmates
2. docker create --env-file .env -it --name fastapi_padel -p 127.0.0.1:8000:8000 fastapi_padelmates
3. docker start -i fastapi_padel
4. Access the API at http://127.0.0.1:8000 or http://localhost:8000 or http://0.0.0.0:8000


5. docker images
6. docker ps -a
7. docker stop fastapi_padel
8. docker rm fastapi_padel
9. docker rmi fastapi_padelmates
```

## Coding Standards

### Naming Conventions

- Classes: PascalCase
- Functions: snake_case
- Variables: snake_case
- Constants: ALL_CAPS

### Code Formatting

- Use `black` to format code.
- Use `flake8` to check for PEP8 compliance.
- Use `mypy` to check for type hints.
- Use `tox` to run all of the above.

### Code Documentation

- Use google style docstrings.

### Date and Time

- All the internal date and time formats will be in UTC timezone, unix timestamp.
- We will receive date and time from the frontend in UTC timezone, unix timestamp.
- And we will send date and time to the frontend in UTC timezone, unix timestamp.
- We may use `int(time.time())` to get the current time in `seconds` since the epoch in UTC: unix timestamp.
- https://docs.python.org/3/library/time.html

```bash
import time
(int(time.time() * 1000))
```

## Custom Tests

After running the server, run the following commands to test the codebase:
You can also create new tests in `test_request.py` and `test_TestClient.py` and run them.

```
python test_request.py
python test_TestClient.py
```

## Instructions For Pushing Code.

Before final push, do the following:

```
1. test codebase
2. sort imports: isort . && black .
4. Use "Sourcery" to refactor code in VS Code.
https://marketplace.visualstudio.com/items?itemName=sourcery.sourcery
5. flake8 . && mypy . && mypy --python-version=3.7 .
7. tox
8. pull from 'dev' branch
9. handle merge conflicts
10. follow 2-7 again
11. push to your branch
12. make sure all tests pass
13. make a pull request to 'dev' branch
```

## Notes

`test_request.py` tests the code by calling API endpoints with `requests` library.
`test_TestClient.py` tests the code by calling API endpoints with `TestClient` from `starlette.testclient` library.

Some issues with calling them from the FastAPI docs due to issues between Pydantic Base Classes and Async functions. Fixes are TODO. So, use custom_tests for now

## Codebase Structure

```
.
├── configs
│   ├── config.py
│   ├── configs_readme.md
│   ├── __init__.py
│   └── py.typed
├── database
│   ├── activity_joins.py
│   ├── activity_records.py
│   ├── bookings.py
│   ├── chatChannelMembers.py
│   ├── chatchannels.py
│   ├── club_credits.py
│   ├── clubs.py
│   ├── courts.py
│   ├── credit_packages.py
│   ├── discounts.py
│   ├── event_logs.py
│   ├── feedbacks.py
│   ├── firebase_connect.py
│   ├── followers.py
│   ├── gameinterests.py
│   ├── guest_users.py
│   ├── __init__.py
│   ├── locations.py
│   ├── matches.py
│   ├── membershipinfos.py
│   ├── memberships.py
│   ├── mongo_connect.py
│   ├── notificationchannels.py
│   ├── notificationsettings.py
│   ├── price_lists.py
│   ├── prices.py
│   ├── py.typed
│   ├── rewards.py
│   ├── sessions.py
│   ├── slots.py
│   ├── staffs.py
│   ├── subscriptions.py
│   ├── tournament_matchmaking.py
│   ├── tournaments.py
│   ├── trainings.py
│   ├── transactions.py
│   ├── users.py
│   └── utils.py
├── documentation
│   └── ERDiag.drawio
├── external_endpoint
│   ├── CONSTANTS.py
│   ├── __init__.py
│   ├── memberships.py
│   ├── qt_systems.py
│   └── refunds.py
├── .github
│   └── workflows
│       └── tests.yml
├── internal
│   ├── activity
│   │   ├── activity.py
│   │   ├── booking.py
│   │   ├── matchmaking.py
│   │   └── participant.py
│   ├── admin
│   │   ├── cron_task.py
│   │   └── log.py
│   ├── authentication
│   │   ├── forgot.py
│   │   ├── login.py
│   │   ├── logout.py
│   │   ├── permission.py
│   │   ├── role_check.py
│   │   ├── signup.py
│   │   ├── token.py
│   │   └── verify.py
│   ├── club
│   │   ├── account.py
│   │   ├── chat_channels.py
│   │   ├── coach.py
│   │   ├── court.py
│   │   ├── credit_package.py
│   │   ├── discount_code.py
│   │   ├── event_logs.py
│   │   ├── follower.py
│   │   ├── info.py
│   │   ├── invite.py
│   │   ├── league.py
│   │   ├── member.py
│   │   ├── membership.py
│   │   ├── notification.py
│   │   ├── price_list.py
│   │   ├── price.py
│   │   ├── reward_history.py
│   │   ├── reward.py
│   │   ├── slot.py
│   │   └── statistics.py
│   ├── player
│   │   ├── player_activity.py
│   │   ├── player_booking.py
│   │   ├── player_club_info.py
│   │   ├── player_credit.py
│   │   └── player_membership.py
│   ├── series_games
│   │   ├── division.py
│   │   ├── league.py
│   │   ├── match.py
│   │   ├── season.py
│   │   ├── series.py
│   │   └── team.py
│   ├── staff
│   │   └── staff.py
│   ├── __init__.py
│   ├── mail.py
│   └── py.typed
├── log
│   ├── __init__.py
│   └── logging.py
├── middleware
├── routers
│   ├── activity
│   │   ├── activity.py
│   │   ├── book_court.py
│   │   ├── description.py
│   │   ├── match.py
│   │   ├── tournament.py
│   │   └── training.py
│   ├── admin
│   │   └── log.py
│   ├── authentication
│   │   ├── forgot.py
│   │   ├── login.py
│   │   ├── logout.py
│   │   ├── permission.py
│   │   ├── signup.py
│   │   └── token.py
│   ├── club
│   │   ├── account.py
│   │   ├── coach.py
│   │   ├── court.py
│   │   ├── credit_package.py
│   │   ├── credit.py
│   │   ├── discount_code.py
│   │   ├── event_logs.py
│   │   ├── follower.py
│   │   ├── info.py
│   │   ├── member.py
│   │   ├── membership.py
│   │   ├── notification.py
│   │   ├── payment.py
│   │   ├── price_list.py
│   │   ├── price.py
│   │   ├── reward.py
│   │   ├── slot.py
│   │   ├── statistics.py
│   │   └── verify.py
│   ├── club_non_reg
│   │   └── location.py
│   ├── guest
│   │   └── guest_user.py
│   ├── mobile
│   │   └── mobile.md
│   ├── player
│   │   ├── player_activity.py
│   │   ├── player_booking.py
│   │   ├── player_club_info.py
│   │   ├── player_membership.py
│   │   └── player.py
│   ├── series_games
│   │   ├── division.py
│   │   ├── league.py
│   │   ├── season.py
│   │   ├── series_games_match.py
│   │   └── team.py
│   ├── staff
│   │   └── staff.py
│   ├── support
│   │   ├── chat_channels.py
│   │   └── support.md
│   ├── webportal
│   │   └── webportal.md
│   ├── website
│   │   └── website.md
│   ├── __init__.py
│   └── py.typed
├── schemas
│   ├── database_schema
│   │   ├── club_activity_joins.py
│   │   ├── club_activity_records.py
│   │   ├── event_logs.py
│   │   └── py.typed
│   ├── request_schema
│   │   └── py.typed
│   ├── response_schema
│   │   ├── club_clubs.py
│   │   ├── event_logs.py
│   │   └── py.typed
│   ├── activity_join.py
│   ├── booking.py
│   ├── chatchannel.py
│   ├── club_credits.py
│   ├── club.py
│   ├── coach.py
│   ├── court.py
│   ├── credit_package.py
│   ├── discount_code.py
│   ├── event_logs.py
│   ├── follower.py
│   ├── generic.py
│   ├── guest_user.py
│   ├── __init__.py
│   ├── invite.py
│   ├── league.py
│   ├── location.py
│   ├── login.py
│   ├── member.py
│   ├── membership.py
│   ├── notificationchannels.py
│   ├── player_booking.py
│   ├── player_club_info.py
│   ├── player_membership.py
│   ├── player.py
│   ├── player_user.py
│   ├── price_list.py
│   ├── price.py
│   ├── py.typed
│   ├── reward.py
│   ├── series_games_match.py
│   ├── slot.py
│   ├── staff.py
│   ├── team.py
│   └── translation.py
├── test
│   ├── club
│   │   ├── __init__.py
│   │   └── test_league.py
│   ├── series_games
│   │   ├── __init__.py
│   │   └── team.py
│   ├── __init__.py
│   └── test_club_follower.py
├── utils
│   ├── currency.csv
│   ├── currency.py
│   ├── __init__.py
│   ├── translation.json
│   ├── translation.py
│   └── util.py
├── 23_transfer_to_club_followers.log
├── apprunner.yaml
├── CONSTANTS.py
├── docker-compose.yml
├── dockerfile
├── .dockerignore
├── .env
├── .gitignore
├── main.py
├── procfile
├── pyproject.toml
├── README.md
├── requirements_dev.txt
├── requirements.txt
├── setup.cfg
└── tox.ini
```

Generated with `tree` and then some manual formatting:

```
sudo apt install tree
tree --dirsfirst -a -I "__pycache__|.git|.mypy_cache|.tox|Webportal_backend.egg-info"
```

