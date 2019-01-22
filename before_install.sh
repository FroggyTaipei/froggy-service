#!/bin/sh

if [ "$TRAVIS_BRANCH" == "master" ] && [ "$TRAVIS_PULL_REQUEST" == "false" ];
then
  openssl aes-256-cbc -K $encrypted_1fa28bd21641_key -iv $encrypted_1fa28bd21641_iv -in .env.enc -out .env -d
  openssl aes-256-cbc -K $encrypted_1fa28bd21641_key -iv $encrypted_1fa28bd21641_iv -in gs_credential.json.enc -out backend/gs_credential.json -d
else
  sudo cp .env.example .env
  sudo touch backend/gs_credential.json
fi
