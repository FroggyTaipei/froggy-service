# Froggy's service
![travis-ci](https://travis-ci.org/FroggyTaipei/froggy-service.svg?branch=master)

Project setup using [cookiecutter-django-vue](https://github.com/vchaptsev/cookiecutter-django-vue)

### Contribution

See our [contributing guide](CONTRIBUTING.md).

### Development

Create your own `.env` file at root, e.g. using `.env.example`:
```
$ sudo cp .env.example .env
```

Use `--build` to rebuild image, `-d` to run containers in the background :
```
$ docker-compose up --build
```

Use `-v` to clean volume while stop containers:
```
$ docker-compose down -v
```

Run production:
```
$ docker-compose -f docker-compose-prod.yml up
$ docker-compose -f docker-compose-prod.yml down
```

Base on your operating system, **missing bindings** might happen:
```
$ docker-compose up
...
Node Sass could not find a binding for your current environment: Linux/musl 64-bit with Node.js 10.x
```
Try mounting container's node_module to volume with a different name, 
e.g. changing `docker-compose.yml`:
```yaml
volumes:
  node_modules_volume:

frontend:
  image: node:10-alpine
  command: npm run serve
  volumes:
    - ./.env:/app/.env:ro
    - ./frontend:/app
    - node_modules_volume:/usr/src/app/node_modules
  working_dir: /app
  restart: on-failure
```
See: [Docker ALPINE Linux throws node-sass missing binding error](https://github.com/sass/node-sass/issues/2165) 

### Deploy

Run the app in Kubernetes
The folder k8s-specifications contains the yaml specifications of the App's services.

First create the app namespace
```
$ kubectl create namespace app
```

Create secrets
```
$ kubectl create secret generic environs --from-env-file .env --namespace app
```

Run the following command to create the deployments and services objects:
```
$ kubectl create -f k8s-specifications/
```
```
ingress.extensions/ingress created
deployment.extensions/api created
service/api-service created
deployment.extensions/postgres created
service/postgres created
deployment.extensions/nginx created
service/nginx-service created
```

Clean up
```
$ kubectl delete -f k8s-specifications/
```

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
