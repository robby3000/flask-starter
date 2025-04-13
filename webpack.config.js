const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = (env, argv) => {
  const isProduction = argv.mode === 'production';

  return {
    entry: {
        main: [
            './app/static/src/js/main.js',
            './app/static/src/css/main.css'
        ]
    },
    output: {
      filename: '[name].bundle.js', // Output JS bundle name
      path: path.resolve(__dirname, 'app/static/dist'), // Output directory for bundles
      clean: true, // Clean the output directory before each build
    },
    mode: isProduction ? 'production' : 'development',
    devtool: isProduction ? false : 'source-map', // Add source maps for development
    module: {
      rules: [
        {
          test: /\.css$/,
          use: [
            MiniCssExtractPlugin.loader, // Extract CSS into separate files
            'css-loader', // Translates CSS into CommonJS
            {
              loader: 'postcss-loader', // Process CSS with PostCSS (for Tailwind)
              options: {
                postcssOptions: {
                  config: path.resolve(__dirname, 'postcss.config.js'),
                },
              },
            },
          ],
        },
        // Add rules for other assets like images or fonts if needed later
        // {
        //   test: /\.(png|svg|jpg|jpeg|gif)$/i,
        //   type: 'asset/resource',
        // },
      ],
    },
    plugins: [
      new MiniCssExtractPlugin({
        filename: '[name].bundle.css', // Output CSS bundle name
      }),
    ],
    optimization: {
      minimize: isProduction, // Minimize CSS and JS only in production
    },
  };
};