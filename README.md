# DOCKER-PYTHON-GEOSERVER
Test environment to verify the connection between two images.

The Geoserver's Docker image used into docker compose is [this](https://github.com/MaxDragonheart/docker-geoserver).
-----


# TEST without docker compose
Build: `docker build -t LAYER-NAME .`

Build with args: `docker build --build-arg ARG1=VALUE1 --build-arg ARG2=VALUE2 -t LAYER-NAME .`

Run and access to container: `docker run -it LAYER-NAME` 
Run and access to container using `.env`: `docker run --env-file /home/max/DEV/TEST/python-geoserver/.env -it LAYER-NAME` 

Start container: `docker container run -it -d --name CONTAINER-NAME -p 8081:8080 LAYER-NAME`

# TEST with docker compose

Build: `docker-compose -f docker-compose.yml up -d --build`

Build for Compose 1.2: `docker compose -f docker-compose.yml up -d --build`

# UTILS
List of active container: `docker ps`

List of images: `docker images`

Purge images and volumes: `docker system prune -a --volumes`

