#!/bin/sh

if [ "$TRAVIS_BRANCH" == "master" ] && [ "$TRAVIS_PULL_REQUEST" == "false" ];
then
  openssl aes-256-cbc -K $encrypted_1fa28bd21641_key -iv $encrypted_1fa28bd21641_iv -in .env.enc -out .env -d
else
  sudo cp .env.example .env
fi
