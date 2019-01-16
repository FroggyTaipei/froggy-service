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
