# WWW

### Eslint setup

VSCode settings.json

```
{
  "eslint.validate": [
    {
      "language": "vue",
      "autoFix": true //Autofix any fixable errors when linting
    },
    {
      "language": "javascript",
      "autoFix": true
    },
    {
      "language": "javascriptreact",
      "autoFix": true
    }
  ],
  "eslint.autoFixOnSave": true,
  "vetur.validation.template": false
}
```

.eslintrc.js

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

.eslintignore

```
build/*.js
```

### Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


# API

### Requires

    $ cd src

    $ pip install -r requirements.txt

### Django settings.py
Create and edit local.py in src/froggy_service/settings to configing your database parameter(notice **USER**, **PASSWORD** below) and **SECRET_KEY**,

See [Django tutorial](https://docs.djangoproject.com/en/dev/intro/tutorial01/) or maybe use [online generator](http://www.miniwebtool.com/django-secret-key-generator/) to get SECRET_KEY for convenience
```
SECRET_KEY = '' # put random string inside and don't share it with anybody.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mydb', # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '', # Set to empty string for default.
    }
}
```
Because local.py is list in .gitignore, so this file won't be appear in source control, for safety.