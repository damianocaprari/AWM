import colors from 'vuetify/es5/util/colors'

export default {
  mode: 'universal',
  server:{
    port: 3000,
    host: '0.0.0.0'
  },
  /*
  ** Headers of the page
  */
  head: {
    //titleTemplate: '%s - ' + process.env.npm_package_name,
    titleTemplate: '%s',
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/d20_favicon.jpg' }
    ]
  },
  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },
  /*
  ** Global CSS
  */
  css: ['~/assets/css/transitions.css',
  ],
  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
    '~/api/init.js',
    '~/plugins/axios.js',
    '~/plugins/utils.js',
  ],
  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [
    '@nuxtjs/vuetify',
  ],
  /*
  ** Nuxt.js modules
  */
  modules: [
    '@nuxtjs/axios'
  ],

  // add this Axios object
  axios: {
    baseURL: "http://localhost:8000/api"
  },

  /*
  ** vuetify module configuration
  ** https://github.com/nuxt-community/vuetify-module
  */
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: false,
      themes: {
        light: {
          primary: colors.grey.darken4,
          onprimary: colors.shades.white,
          accent: colors.red.accent4,
          onaccent: colors.shades.white,
          secondary: colors.grey.darken2,
          onsecondary: colors.shades.white,
          success: colors.green.accent3,
          onsuccess: colors.shades.black,
          info: colors.lightBlue.lighten1,
          oninfo: colors.shades.black,
          warning: colors.amber.base,
          onwarning: colors.shades.black,
          error: colors.deepOrange.accent4,
          onerror: colors.shades.white
        },
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        }
      }
    }
  },
  /*
  ** Build configuration
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    extend (config, ctx) {
    }
  },
  router: {
    middleware: [
      'auth',
    ]
  }
}
