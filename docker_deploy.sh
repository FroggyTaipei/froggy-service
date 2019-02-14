#!/usr/bin/env bash

set -e

RELEASE_NGINX=gcr.io/${GOOGLE_PROJECT_ID}/${NGINX_IMAGE}
RELEASE_API=gcr.io/${GOOGLE_PROJECT_ID}/${API_IMAGE}
STAGE_NGINX=gcr.io/${GOOGLE_PROJECT_ID}/${STAGE_NGINX_IMAGE}
STAGE_API=gcr.io/${GOOGLE_PROJECT_ID}/${STAGE_API_IMAGE}
PUBLIC_NGINX=${DOCKER_ORG}/${NGINX_IMAGE}
PUBLIC_API=${DOCKER_ORG}/${API_IMAGE}

if [ "$TRAVIS_BRANCH" == "master" ] && [ "$TRAVIS_PULL_REQUEST" == "false" ]; then

    # Use Credential file to access google cloud
    gcloud auth activate-service-account --key-file gs_credential.json
    gcloud auth configure-docker

    # =================================== Release ===================================
    sudo cp .env.prod .env

    docker image build -t $RELEASE_API:$TRAVIS_COMMIT ./backend;
    docker image build -t $RELEASE_NGINX:$TRAVIS_COMMIT -f nginx/k8s.Dockerfile .;
    docker image tag $RELEASE_API:$TRAVIS_COMMIT $RELEASE_API:latest;
    docker image tag $RELEASE_NGINX:$TRAVIS_COMMIT $RELEASE_NGINX:latest;
    docker push $RELEASE_NGINX;
    docker push $RELEASE_API;

    # =================================== Stage =====================================
    sudo cp .env.stage .env

    docker image build -t $STAGE_API:$TRAVIS_COMMIT ./backend;
    docker image build -t $STAGE_NGINX:$TRAVIS_COMMIT -f nginx/k8s.Dockerfile .;
    docker image tag $STAGE_API:$TRAVIS_COMMIT $STAGE_API:latest;
    docker image tag $STAGE_NGINX:$TRAVIS_COMMIT $STAGE_NGINX:latest;
    docker push $STAGE_NGINX;
    docker push $STAGE_API;

    # =================================== GKE =======================================

    # Access cluster
    gcloud --quiet config set project $GOOGLE_PROJECT_ID
    gcloud --quiet config set container/cluster $CLUSTER
    gcloud --quiet config set compute/zone $ZONE
    gcloud --quiet container clusters get-credentials $CLUSTER

    # Release deployment update
    kubectl set image deployment/${NGINX_DEPLOYMENT} ${NGINX_CONTAINER}=$RELEASE_NGINX:$TRAVIS_COMMIT;
    kubectl set image deployment/${API_DEPLOYMENT} ${API_CONTAINER}=$RELEASE_API:$TRAVIS_COMMIT;

    # Stage deployment update
    kubectl set image deployment/${NGINX_DEPLOYMENT} --namespace=stage ${NGINX_CONTAINER}=$STAGE_NGINX:$TRAVIS_COMMIT;
    kubectl set image deployment/${API_DEPLOYMENT} --namespace=stage ${API_CONTAINER}=$STAGE_API:$TRAVIS_COMMIT;

    # =================================== Public ====================================
    sudo cp .env.example .env
    sudo cp /dev/null gs_credential.json
    sudo cp /dev/null backend/gs_credential.json

    # Rebuild both and push to docker hub
    docker login -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD";
    docker image build -t $PUBLIC_API:$TRAVIS_COMMIT ./backend;
    docker image build -t $PUBLIC_NGINX:$TRAVIS_COMMIT -f nginx/k8s.Dockerfile .;
    docker image tag $PUBLIC_API:$TRAVIS_COMMIT $PUBLIC_API:latest;
    docker image tag $PUBLIC_NGINX:$TRAVIS_COMMIT $PUBLIC_NGINX:latest;
    docker push $PUBLIC_NGINX;
    docker push $PUBLIC_API;

fi
