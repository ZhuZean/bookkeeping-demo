<template>
  <div class="home">
    <div id="home-container" class="container">
      <div class="row">
        <div class="col">
          <Summary></Summary>
        </div>
        <div class="col ml-5">
          <add-record></add-record>
          <hr class="mt-3 mb-3" style="border: 0; border-top: 2px solid #FFC107;"/>
          <bill-detail class="mt-4"></bill-detail>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Summary from "./components/Summary.vue"
import AddRecord from "./components/AddRecord.vue"
import BillDetail from "./components/BillDetail.vue"

export default {
  name: "Home",
  components: {
    Summary,
    AddRecord,
    BillDetail
  },
};
</script>

<style lang="scss">
#home-container {
  margin-top: 10em;
}
</style>
