// vue.config.js

const CompressionPlugin = require('compression-webpack-plugin')

module.exports = {
  lintOnSave: false,
  configureWebpack: config => {
    return {
      plugins: [
        new CompressionPlugin({
          algorithm: 'gzip',
          test: /\.js$|\.html$|.\css/,
          threshold: 10240,
          deleteOriginalAssets: false
        })]
    }
  },
  devServer: {
    hot: true,
    hotOnly: true,
    disableHostCheck: true,
    historyApiFallback: true,
    public: '0.0.0.0:8000',
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
      'Access-Control-Allow-Headers': 'X-Requested-With, content-type, Authorization'
    },
    watchOptions: {
      poll: 1000,
      ignored: '/app/node_modules/'
    }
  }
}
