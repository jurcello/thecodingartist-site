const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const { VueLoaderPlugin } = require("vue-loader");
const path = require('path');
const devMode = process.env.NODE_ENV !== 'production';

module.exports = {
  entry: ['./src/js/index.js', './src/sass/zon.scss'],
  output: {
    filename: 'js/zon.js',
    path: path.resolve(__dirname, '../codingartist/codingartist/static')
  },
  plugins: [
    new MiniCssExtractPlugin({
      // Options similar to the same options in webpackOptions.output
      // both options are optional
      filename: devMode ? 'css/zon.css' : 'css/zon.[hash].css',
      chunkFilename: devMode ? 'css/[id].css' : 'css/[id].[hash].css',
    }),
  ],
  module: {
    rules: [
      {
        test: /\.scss$/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader,
          },
          {
            loader: 'css-loader',
            options: {
              importLoaders: 1
            }
          },
          {
            loader: 'postcss-loader'
          },
          {
            loader: "sass-loader",
            options : {
              includePaths: [path.resolve(__dirname, 'node_modules')]
            },
          },
        ]
      }
    ]
  },
};