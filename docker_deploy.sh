#!/usr/bin/env bash
if [ "$TRAVIS_BRANCH" == "master" ] && [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
    docker-compose exec backend sh -c "python manage.py collectstatic --noinput --verbosity 0"

    docker login -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD";
    docker image build -t froggytaipei/froggy-service-nginx:"${GIT_COMMIT}" -f nginx/Dockerfile .;
    docker image build -t froggytaipei/froggy-service-api:"${GIT_COMMIT}" ./backend;
    docker push froggytaipei/froggy-service-nginx;
    docker push froggytaipei/froggy-service-api;

    gcloud auth print-access-token | docker login -u oauth2accesstoken --password-stdin https://gcr.io
    gcr_nginx_url = gcr.io/${GOOGLE_PROJECT_ID}/froggy-service-nginx:"${GIT_COMMIT}"
    gcr_api_url = gcr.io/${GOOGLE_PROJECT_ID}/froggy-service-api:"${GIT_COMMIT}"
    docker image build -t $gcr_nginx_url -f k8s/Dockerfile .;
    docker image build -t $gcr_api_url ./backend;
    docker push $gcr_nginx_url
    docker push $gcr_api_url
    kubectl set image deployment/nginx-stage nginx-stage=$gcr_nginx_url
    kubectl set image deployment/api-stage nginx-stage=$gcr_api_url
fi
