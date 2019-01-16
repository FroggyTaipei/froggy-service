# Froggy's service
Project setup using [cookiecutter-django-vue](https://github.com/vchaptsev/cookiecutter-django-vue)

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
$ docker-compose -f docker-compose-prod.yml up --build
$ docker-compose -f docker-compose-prod.yml down -v
```

Base on your operating system, **missing bindings** might happen:
```
$ docker-compose up --build
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


### Architecture

![Architecture diagram](architecture.png)
