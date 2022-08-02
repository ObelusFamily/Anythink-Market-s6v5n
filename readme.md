# Welcome to the Anythink Market repo

To start the app use Docker. It will start both frontend and backend, including all the relevant dependencies, and the db.

Please find more info about each part in the relevant Readme file ([frontend](frontend/readme.md) and [backend](backend/README.md)).

## Development

When implementing a new feature or fixing a bug, please create a new pull request against `main` from a feature/bug branch and add `@vanessa-cooper` as reviewer.

## Docker Deployment

Install Docker if you have not already. https://docs.docker.com/get-docker/

Run `docker-compose up` to create the containers.

User get to the command line of the created containers through the Docker GUI/App or run `docker exec -it container-name sh` to access it from the terminal.

Run `ls` to orientate yourself and make sure you are in the right directory before running commands!!!

## Migrating

`docker exec -it anythink-backend sh` and then `cd backend` to get to the directory where you should run `rails db:migrate`

