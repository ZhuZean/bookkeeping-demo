import { createI18n } from 'vue-i18n'

const numberFormats = {
    'en-US': {
      currency: {
        style: 'currency', currency: 'USD'
      }
    },
    'ja-JP': {
      currency: {
        style: 'currency', currency: 'JPY', currencyDisplay: 'symbol'
      }
    }
}

const dateTimeFormats = {
  'en-US': {
    short: {
      year: 'numeric', month: 'short', day: 'numeric'
    },
    long: {
      year: 'numeric', month: 'short', day: 'numeric',
      weekday: 'short', hour: 'numeric', minute: 'numeric'
    }
  },
  'ja-JP': {
    short: {
      year: 'numeric', month: 'short', day: 'numeric'
    },
    long: {
      year: 'numeric', month: 'short', day: 'numeric',
      weekday: 'short', hour: 'numeric', minute: 'numeric', hour12: true
    },
    normal: {
      year: 'numeric', month: 'short', day: 'numeric',
      hour: 'numeric', minute: 'numeric', hour12: true
    }
  }
}

function loadLocaleMessages() {
  const locales = require.context(
    "./locales",
    true,
    /[A-Za-z0-9-_,\s]+\.json$/i
  );
  const messages:any = {};
  locales.keys().forEach(key => {
    const matched = key.match(/([A-Za-z0-9-_]+)\./i)
    if (matched && matched.length > 1) {
      const locale = matched[1]
      messages[locale] = locales(key)
    }
  });
  return messages
}

const i18n = createI18n({
  locale: 'en',
  numberFormats,
  dateTimeFormats,
  messages: loadLocaleMessages()
})

export default i18n