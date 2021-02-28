<template>
  <v-pagination
    v-model="page"
    :pages="pageCount"
    :range-size="1"
    active-color="#DCEDFF"
    @update:modelValue="clickHandler"
  />
</template>

<script>
import VPagination from "vue3-pagination"
import "vue3-pagination/dist/vue3-pagination.css"

export default {
  name: 'Paginator',
  components: {
     VPagination
  },
  data() {
    return {
      page: 1
    }
  },
  props: {
    pageCount: {
      type: Number,
      required: true
    },
    clickHandler: {
      type: Function,
      default: function() {
        // do nothing.
      }
    }
  }
}
</script>