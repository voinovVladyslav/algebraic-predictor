# Local setup

- Create .env file using .env.example

```bash
cp .env.example .env
```

- build container

```bash
docker compose build
```

- create super user

```bash
docker compose run --rm backend python manage.py createsuperuser
```

- run application

```bash
docker compose up
```

## Useful commands

- run any django command

```bash
docker compose run --rm backend <command>
# e.g. apply migrations
docker compose run --rm backend python manage.py migrate
```

## Links

- admin site located at [127.0.0.1:8000/admin](https://127.0.0.1:8000/admin)
- swagger documentation located at [127.0.0.1:8000/api/docs](https://127.0.0.1:8000/api/docs)
