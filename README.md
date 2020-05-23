# Froggy's service

<a href="https://github.com/vchaptsev/cookiecutter-django-vue">
    <img src="https://img.shields.io/badge/built%20with-Cookiecutter%20Django%20Vue-blue.svg" />
</a>

### Contribution

See our [contributing guide](CONTRIBUTING.md).

### Development

Download [Docker Desktop](https://www.docker.com/products/docker-desktop) for Mac or Windows.
[Docker Compose](https://docs.docker.com/compose) will be automatically installed.
On Linux, make sure you have the latest version of [Compose](https://docs.docker.com/compose/install/).

**Linux Containers**

The Linux stack uses `Python`, `Node.js`, with `Postgres` for storage, `Redis` for caching and `Nginx` for local proxying.

To save your time from image rebuild, pull the cache image from our [DockerHub registry](https://hub.docker.com/r/froggytaipei):
```
$ make pull-cache
```

Create your own `.env` file at root, e.g. using `.env.example`:
```
$ cp .env.example .env
```

Start services, add `--build` to rebuild image, `-d` to run containers in the background :
```
$ docker-compose up
```

Stop services, add `-v` to clean volume while stop containers:
```
$ docker-compose down -v
```

### Deployment

Deploy and manage Kubernetes deployment with [helm chart](helm/froggy-service).

### Architecture

![Architecture diagram](architecture.png)

### Licenses
* Copyright (C) 2019 - 2019 台北市議員邱威傑辦公室. All rights reserved.
* Distributed under the MIT

Media
* Distributed under the CC0 1.0 Universal

Data
* Try our API via [Swagger](https://service.froggychiu.com/api/swagger/)
* Distributed under the CC BY 4.0
