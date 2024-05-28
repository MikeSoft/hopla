# Variables
DOCKER_COMPOSE = docker-compose
PROJECT_NAME = losfunables

# Comandos
.PHONY: build clean deploy

stop:
	$(DOCKER_COMPOSE) stop

# Construir el proyecto desde cero
build:
	$(DOCKER_COMPOSE) build
	$(DOCKER_COMPOSE) up -d

# Limpiar volúmenes y contenedores
clean:
	$(DOCKER_COMPOSE) down --volumes --remove-orphans

deploy:
	$(DOCKER_COMPOSE) up -d --force-recreate

bweb:
	$(DOCKER_COMPOSE) build web
	$(DOCKER_COMPOSE) up -d web
