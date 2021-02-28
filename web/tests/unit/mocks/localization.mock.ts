// To fix TypeError: _vm.$t is not a function
// https://github.com/kazupon/vue-i18n/issues/323
const localization:any = {
    $t: () => {},
    $n: () => {},
    $d: () => {}
}

export default localization
