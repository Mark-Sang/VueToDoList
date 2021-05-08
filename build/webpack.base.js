const path = require('path')

const VueLoaderPlugin = require('vue-loader/lib/plugin')

const HtmlWebpackPlugin = require('html-webpack-plugin')

const { CleanWebpackPlugin } = require('clean-webpack-plugin')


module.exports = {
    //打包入口
    entry: './src/main.js',
    //打包出口
    output: {
        filename: 'app.js',
        path: path.resolve(__dirname, '../dist')
    },
    //打包规则
    module: {
        rules: [{
            test: /\.js$/,
            exclude: /node_modules/,
            loader: "babel-loader"
        }, {
            test: /\.vue$/,
            loader: 'vue-loader'
        }, {
            test: /\.(jpg|jpeg|png|svg|bmp)$/,
            loader: 'url-loader',
            options: {
                name: '[name].[ext]',
                limit: 2048
            }
        }, {
            test: /\.css$/,
            use: ['style-loader', 'css-loader']
        }, {
            test: /\.styl(us)?$/,
            use: ['style-loader', 'css-loader',
                'postcss-loader', 'stylus-loader']
        }, {
            test: /\.(eot|svg|ttf|woff|woff2)(\?\S*)?$/,
            loader: 'file-loader'
        }]
    },
    //插件
    plugins: [
        new VueLoaderPlugin(),
        new HtmlWebpackPlugin({
            template: './index.html'
        }),
        new CleanWebpackPlugin(),
    ],
    resolve: {
        alias: {
            'vue': 'vue/dist/vue.js'
        }
    }
}