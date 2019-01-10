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
Try mounting container's node_module to directory with different name, 
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

### Frontend

Project setup

    npm install

Compiles and hot-reloads for development

    npm run serve


Compiles and minifies for production

    npm run build


Run your tests

    npm run test


Lints and fixes files

    npm run lint


Customize configuration
* See [Configuration Reference](https://cli.vuejs.org/config/).
* VSCode settings.json
    ```
    {
        "vetur.validation.template": false,
        "eslint.autoFixOnSave": true,
        "eslint.validate": [
            "javascript",
            "javascriptreact",
            { "language": "vue", "autoFix": true }
        ]
    }
    ```
* .eslintrc.js
    ```
    //https://vuejs.github.io/eslint-plugin-vue/user-guide/
    module.exports = {
      env: {
        browser: true
      },
      extends: [
        // add more generic rulesets here, such as:
        'plugin:vue/strongly-recommended',
        'standard'
      ],
      rules: {
        // override/add rules settings here, such as:
        'vue/html-closing-bracket-newline': ['error', {
          'multiline': 'never'
        }]
      }
    }
    ```
* .eslintignore
    ```
    build/*.js
    ```

### Backend

Requires

    pip install -r backend/requirements.txt

Django configuration

* environment variable

  We use [django-environ](https://github.com/joke2k/django-environ), it's more easy for docker image building and CI testing. You might want to change it base on how your variable in Django settings are passing.
  For safety, we list `.env` in .gitignore.
