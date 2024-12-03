/**
 * plugins/vuetify.js
 *
 * Framework documentation: https://vuetifyjs.com`
 */

// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

// Composables
import { createVuetify } from 'vuetify'

// https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides
export default createVuetify({
  theme: {
    themes: {
      light: {
        dark: false,
        colors: {
          primary: "#5E5343",
          secondary: "#AEAD87",
          info: "#D8B89B",
          success: "#506344",
          error: "#CB7C39",
          cardbackground: "#EEEEED"
        }
      },
    },
  },
})
