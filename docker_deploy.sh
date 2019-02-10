#!/usr/bin/env bash

set -e

if [ "$TRAVIS_BRANCH" == "master" ] && [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
    docker login -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD";
    docker image build -t ${DOCKER_ORG}/${NGINX_IMAGE}:$TRAVIS_COMMIT -f nginx/Dockerfile .;
    docker image build -t ${DOCKER_ORG}/${API_IMAGE}:$TRAVIS_COMMIT ./backend;
    docker push ${DOCKER_ORG}/${NGINX_IMAGE};
    docker push ${DOCKER_ORG}/${API_IMAGE};

    gcloud auth activate-service-account --key-file gs_credential.json
    gcloud auth configure-docker

    docker image build -t gcr.io/${GOOGLE_PROJECT_ID}/${NGINX_IMAGE}:$TRAVIS_COMMIT -f k8s/Dockerfile .;
    docker image tag ${DOCKER_ORG}/${API_IMAGE}:$TRAVIS_COMMIT gcr.io/${GOOGLE_PROJECT_ID}/${API_IMAGE}:$TRAVIS_COMMIT;
    docker push gcr.io/${GOOGLE_PROJECT_ID}/${NGINX_IMAGE};
    docker push gcr.io/${GOOGLE_PROJECT_ID}/${API_IMAGE};

    gcloud --quiet config set project $GOOGLE_PROJECT_ID
    gcloud --quiet config set container/cluster $CLUSTER
    gcloud --quiet config set compute/zone $ZONE
    gcloud --quiet container clusters get-credentials $CLUSTER

    kubectl set image deployment/${NGINX_DEPLOYMENT} ${NGINX_CONTAINER}=gcr.io/${GOOGLE_PROJECT_ID}/${NGINX_IMAGE}:$TRAVIS_COMMIT;
    kubectl set image deployment/${API_DEPLOYMENT} ${API_CONTAINER}=gcr.io/${GOOGLE_PROJECT_ID}/${API_IMAGE}:$TRAVIS_COMMIT;

fi
