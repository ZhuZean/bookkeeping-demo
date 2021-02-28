<template>
  <Header></Header>
  <router-view/>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component'
import Header from '@/layout/Header.vue'

@Options({
  components: {
    Header,
  },
})
export default class Home extends Vue {}
</script>

<style lang="scss">
@import'~bootstrap/dist/css/bootstrap.css'
</style>
