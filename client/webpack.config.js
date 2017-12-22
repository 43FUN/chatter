var webpack = require('webpack');
var path = require('path');
var ExtractTextPlugin = require('extract-text-webpack-plugin');


var BUILD_DIR = path.resolve(__dirname, 'public');
var SRC_DIR = path.resolve(__dirname, 'src');


module.exports = {
    entry: path.resolve(SRC_DIR, 'static/js/index.js'),
    context: __dirname,
    output: {
        path: BUILD_DIR,
        filename: 'bundle.js'
    },
    devtool: '#cheap-module-eval-source-map',
    resolve: {
        extensions: ['.js', '.jsx']
    },
    module: {
        loaders: [
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
                query: {
                    presets: ['env', 'react'],
                    comments: false
                }
            },
            {
                test: /\.scss/,
                use: ExtractTextPlugin.extract({
                    fallback:'style-loader',
                    use: [
                        'css-loader',
                        'sass-loader'
                    ]
                })
            },
            { test: /\.gif$/, loader: 'url-loader', options: { limit: '10000', mimetype: 'image/gif' } },
            { test: /\.jpg$/, loader: 'url-loader', options: { limit: '10000', mimetype: 'image/jpg' } },
            { test: /\.png$/, loader: 'url-loader', options: { limit: '10000', mimetype: 'image/png' } },
            { test: /\.svg/, loader: 'url-loader', options: { limit: '10000', mimetype: 'image/vsg+xml' } },
            { test: /\.(woff|woff2|ttf|eot)/, loader: 'url-loader', options: { limit: 1 } }
        ]
    },
    plugins: [
        new ExtractTextPlugin('bundle.css', {
            allChunks: true
        })
    ]
};