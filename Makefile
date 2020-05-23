BACKEND_CACHE_IMAGE=froggytaipei/froggy-service-api
BACKEND_IMAGE_NAME=froggy-service-api

pull-cache:
	docker pull ${BACKEND_CACHE_IMAGE} && docker tag ${BACKEND_CACHE_IMAGE} ${BACKEND_IMAGE_NAME}

ps:
	docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Ports}}\t{{.Status}}'

flake8:
	docker exec -it backend flake8 --exclude=migrations --ignore=E121,E226,E402,E501,F401,W503 ./
