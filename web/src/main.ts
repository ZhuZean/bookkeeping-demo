/* eslint-disable */
import { createApp } from 'vue'
import App from './App.vue'
import i18n from '@/i18n'
import router from './router'
import store from './store'
import Paginate from './components/Paginate.vue'

// Bootstrap
import 'bootstrap/dist/css/bootstrap.min.css'
import $ from 'jquery'
import 'bootstrap/dist/js/bootstrap.min.js'

// Fontawesome
import { library } from '@fortawesome/fontawesome-svg-core'
import { faSatelliteDish } from '@fortawesome/free-solid-svg-icons'
import { faMoneyBillAlt, faCreditCard, faBuilding } from '@fortawesome/free-regular-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
library.add(faBuilding, faMoneyBillAlt, faCreditCard, faSatelliteDish)

// (window as any).global = window;
// @ts-ignore
window.Buffer = window.Buffer || require('buffer').Buffer;

// date time format
import moment from 'moment'

// sentry
import * as Sentry from '@sentry/browser'
import { Integrations } from '@sentry/tracing'

const app: any = createApp(App).use(store).use(router).use(i18n)
app.component('font-awesome-icon', FontAwesomeIcon)
app.component('paginate', Paginate)
app.mount('#app')

// Global filters
app.config.globalProperties.$filters = {
    dateFormat(dateStr: any, pattern = 'YYYY-MM-DD HH:mm') {
        return moment(dateStr).format(pattern)
    }
}

// error handling
app.config.errorHandler = (err: any, vm: any, info: any) => {
    Sentry.captureException(err)
}

Sentry.init({
    dsn: process.env.VUE_APP_SENTRY_URL,
    integrations: [new Integrations.BrowserTracing()],
    tracesSampleRate: 1.0
})

window.addEventListener('error', (event) => {
    Sentry.captureException(event)
  })
  window.addEventListener('unhandledrejection', (event) => {
    Sentry.captureException(event)
})
