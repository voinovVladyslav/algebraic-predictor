# Algebraic predictor

## Set up

Copy .env file

```bash
cp .env.example .evn
```

Build docker image

```bash
docker build .
```

Init database

```bash
docker compose run --rm backend flask db init
```

Run project

```bash
docker compose up
```

## Other commands

Run any command

```bash
docker compose run --rm backend <command>
```

## List of commands

List every collections

```bash
flask db collections
```

Create admin

```bash
flask db createadmin
```

## To do

- add api documentation (swagger)
- regex validation for
  - email
  - password
  - prject title
