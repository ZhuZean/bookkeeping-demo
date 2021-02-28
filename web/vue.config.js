/* eslint-disable */
const webpack = require("webpack");

module.exports = {
  configureWebpack: {
    mode: 'development',
    plugins: [
      new webpack.ProvidePlugin({
        $: 'jquery',
        jQuery: 'jquery',
        'window.jQuery': 'jquery',
        Popper: ['popper.js', 'default']
      }),
      new webpack.ProvidePlugin({
        process: 'process/browser',
      }),
    ],
    resolve: {
      extensions: [],
      fallback: {
          "http": require.resolve("stream-http"),
          "https": require.resolve("https-browserify"),
          "path": require.resolve("path-browserify"),
          "Buffer": require.resolve("buffer")
      }
    }
  }
}