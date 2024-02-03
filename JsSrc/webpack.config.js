const path = require('path');
const TerserPlugin = require('terser-webpack-plugin');
const HappyPack = require('happypack');
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');
const happyThreadPool = HappyPack.ThreadPool({ size: 6 });
const { CleanWebpackPlugin } = require('clean-webpack-plugin');


module.exports = {
    mode: 'production',
    entry: {
        accounts: './accounts/index.js',
        configurator: './configurator/index.js',
    },
    module: {
        rules: [
            {
                test: [/\.ts$/, /\.js$/],
                use: [
                    {
                        loader: 'happypack/loader?id=babel',
                    },
                ],
            }
        ],
    },
    resolve: {
        extensions: ['.ts', '.js'],
        alias: {
            '@': path.resolve(__dirname, 'src'),
        },
    },
    optimization: {
        minimizer: [new TerserPlugin({
            parallel: true,
            terserOptions: {
            compress: {
                defaults: true,
            },
            mangle: true,
        }})],
        removeAvailableModules: false,
    },
    plugins: [
        new HappyPack({
            id: 'babel',
            threadPool: happyThreadPool,
            loaders: ['babel-loader?cacheDirectory=true'],
        }),
        new BundleAnalyzerPlugin(),
        new CleanWebpackPlugin(),
    ],
    target: 'web',
    output: {
        filename: ({ chunk: { name } }) => {
            return `${name}.js`;
        },
        path: path.resolve(__dirname, '../CustomGuitars/static/webpack_bundles'),
    },
};