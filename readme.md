# Gipsy Avenger

A self-hosted scheduler app that will upgrade or downgrade your EC2 servers for you.

### Features:

1. Log monitoring from the app's dashboard.
2. Instant Slack notifications regarding events.
3. Authentication enabled pages to prevent intrusion

## Self-Hosting

1. Clone the repository into your server.
2. `cd gipsy_avenger && cp .env.example .env`.
3. Set the necessary variables in `.env` file.
4. Please refer to `docs/` for guidance.
5. Now build and deploy the application using `docker-compose -f docker/app.yml build && docker-compose -f docker/app.yml up`.
6. In order to run in detached mode use `docker-compose -f docker/app.yml up -d`.
7. Now the app will be running in `localhost:8000`, write a `nginx` config to proxy pass, if needed.
8. In order to access the admin panel, create a superuser using `docker-compose -f docker/app.yml run web python manage.py createsuperuser`.

Your thoughts, suggestions, feedback, comments and PR's are welcome 😊
