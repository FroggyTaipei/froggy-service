#!/usr/bin/env bash

set -e

RELEASE_NGINX=gcr.io/${GOOGLE_PROJECT_ID}/${NGINX_IMAGE}
RELEASE_API=gcr.io/${GOOGLE_PROJECT_ID}/${API_IMAGE}
STAGE_NGINX=gcr.io/${GOOGLE_PROJECT_ID}/${STAGE_NGINX_IMAGE}
STAGE_API=gcr.io/${GOOGLE_PROJECT_ID}/${STAGE_API_IMAGE}
PUBLIC_NGINX=${DOCKER_ORG}/${NGINX_IMAGE}
PUBLIC_API=${DOCKER_ORG}/${API_IMAGE}

function access_gke_cluster(){
    gcloud auth activate-service-account --key-file $1
    gcloud auth configure-docker
    gcloud --quiet config set project ${GOOGLE_PROJECT_ID}
    gcloud --quiet config set container/cluster ${CLUSTER}
    gcloud --quiet config set compute/zone ${ZONE}
    gcloud --quiet container clusters get-credentials ${CLUSTER}
}

function build_and_push_image(){
  # Use latest image as cache
  docker pull $1:latest || exit 0;
  docker image build -t $1:$2 -f $3 --cache-from $1:latest $4;
  docker image tag $1:$2 $1:latest;
  docker push $1;
}

if [ "$TRAVIS_BRANCH" == "release" ] && [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
    # Access cluster
    access_gke_cluster gs_credential.json

    # Build and push to GCR
    sudo cp .env.prod .env
    build_and_push_image ${RELEASE_API} ${TRAVIS_COMMIT} backend/Dockerfile ./backend
    build_and_push_image ${RELEASE_NGINX} ${TRAVIS_COMMIT} nginx/Dockerfile .

    # Release deployment update
    kubectl set image deployment/${API_DEPLOYMENT} ${API_CONTAINER}=${RELEASE_API}:${TRAVIS_COMMIT};
    kubectl set image deployment/${NGINX_DEPLOYMENT} ${NGINX_CONTAINER}=${RELEASE_NGINX}:${TRAVIS_COMMIT};
fi

if [ "$TRAVIS_BRANCH" == "staging" ] && [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
    # Access cluster
    access_gke_cluster gs_credential.json

    # Build and push to GCR
    sudo cp .env.stage .env
    build_and_push_image ${STAGE_API} ${TRAVIS_COMMIT} backend/Dockerfile ./backend
    build_and_push_image ${STAGE_NGINX} ${TRAVIS_COMMIT} nginx/Dockerfile .

    # Deploy
    kubectl set image deployment/${API_DEPLOYMENT} --namespace=stage ${API_CONTAINER}=${STAGE_API}:${TRAVIS_COMMIT};
    kubectl set image deployment/${NGINX_DEPLOYMENT} --namespace=stage ${NGINX_CONTAINER}=${STAGE_NGINX}:${TRAVIS_COMMIT};
fi

if [ "$TRAVIS_BRANCH" == "master" ] && [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
    sudo cp .env.example .env
    sudo rm backend/gs_credential.json

    # Build and push to DockerHub
    docker login -u="${DOCKER_USERNAME}" -p="${DOCKER_PASSWORD}";
    build_and_push_image ${PUBLIC_API} ${TRAVIS_COMMIT} backend/Dockerfile ./backend
    build_and_push_image ${PUBLIC_NGINX} ${TRAVIS_COMMIT} nginx/Dockerfile .
fi
