#!/bin/sh

if [ "$TRAVIS_BRANCH" == "master" ] && [ "$TRAVIS_PULL_REQUEST" == "false" ];
then
  openssl aes-256-cbc -K $encrypted_1fa28bd21641_key -iv $encrypted_1fa28bd21641_iv -in secrets.tar.enc -out secrets.tar -d
  tar xvf secrets.tar
  sudo cp gs_credential.json backend/gs_credential.json
else
  sudo cp .env.example .env
  sudo touch backend/gs_credential.json
fi
