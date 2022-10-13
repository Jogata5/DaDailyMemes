export DOCKER_BUILDKIT=0
export COMPOSE_DOCKER_CLI_BUILD=0

build:
	docker build --force-rm $(options) -t dadailymemes_website:latest . 
	
build-prod:
	$(MAKE) build options"--target production"

compose-start:
	docker-compose up --remove-orphans $(options)
	
compose_stop:
	docker-compose down --remove-orphans $(options)

compose-manage-py:
	docker-compose run --rm $(option) website python manage.py $(cmd)