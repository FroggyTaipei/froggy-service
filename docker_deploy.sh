#!/usr/bin/env bash

set -e

if [ "$TRAVIS_BRANCH" == "master" ] && [ "$TRAVIS_PULL_REQUEST" == "false" ]; then

    # Use Credential file to access google cloud
    gcloud auth activate-service-account --key-file gs_credential.json
    gcloud auth configure-docker

    # Build image and push to google container registry
    docker image build -t gcr.io/${GOOGLE_PROJECT_ID}/${NGINX_IMAGE}:$TRAVIS_COMMIT -f nginx/k8s.Dockerfile .;
    docker image build -t gcr.io/${GOOGLE_PROJECT_ID}/${API_IMAGE}:$TRAVIS_COMMIT ./backend;
    docker push gcr.io/${GOOGLE_PROJECT_ID}/${NGINX_IMAGE};
    docker push gcr.io/${GOOGLE_PROJECT_ID}/${API_IMAGE};

    # Access cluster
    gcloud --quiet config set project $GOOGLE_PROJECT_ID
    gcloud --quiet config set container/cluster $CLUSTER
    gcloud --quiet config set compute/zone $ZONE
    gcloud --quiet container clusters get-credentials $CLUSTER

    # Rolling update
    kubectl set image deployment/${NGINX_DEPLOYMENT} ${NGINX_CONTAINER}=gcr.io/${GOOGLE_PROJECT_ID}/${NGINX_IMAGE}:$TRAVIS_COMMIT;
    kubectl set image deployment/${API_DEPLOYMENT} ${API_CONTAINER}=gcr.io/${GOOGLE_PROJECT_ID}/${API_IMAGE}:$TRAVIS_COMMIT;

    # Remove secret and deploy to docker hub for public use
    sudo cp .env.example .env
    sudo cp /dev/null gs_credential.json
    sudo cp /dev/null backend/gs_credential.json

    # Rebuild and push to docker hub
    docker login -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD";
    docker image build -t ${DOCKER_ORG}/${NGINX_IMAGE} -f nginx/k8s.Dockerfile .;
    docker image build -t ${DOCKER_ORG}/${API_IMAGE} ./backend;
    docker push ${DOCKER_ORG}/${NGINX_IMAGE};
    docker push ${DOCKER_ORG}/${API_IMAGE};

fi
