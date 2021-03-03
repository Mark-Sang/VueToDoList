
const baseConfig = require('./webpack.base.js')

const { merge } = require('webpack-merge')

const webpack = require('webpack')

const devConfig = {
  mode: 'development',
  //source-map
  devtool: 'eval',
  //devServer配置
  devServer: {
    contentBase: './dist',
    open: true,
    hot: true,
    proxy: {
      '/api': {
        // 此处的写法，目的是为了 将 /api 替换成 http://127.0.0.1:5000/
        target: 'http://127.0.0.1:5000',
        // 允许跨域
        changeOrigin: true,
        ws: true,
        secure: true,
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  },
  //插件
  plugins: [
    new webpack.HotModuleReplacementPlugin()
  ],
}

module.exports = merge(baseConfig, devConfig)