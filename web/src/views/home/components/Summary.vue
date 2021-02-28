<template>
  <div>
    <div id="summary" class="container">
      <h2 class="text-center">{{ $t("Home.Summary.header") }}</h2>
      <p class="h5 text-center">{{ getCurrentDate }}</p>
      <div class="row mt-4">
        <div class="col">
          <h4 class="text-center">{{ $t("Home.Summary.sub_header.income") }}</h4>
        </div>
        <div class="col">
          <h4 class="text-center">{{ $t("Home.Summary.sub_header.expense") }}</h4>
        </div>
      </div>
      <div class="row mt-2">
        <div class="col">
          <h5 class="text-center text-success">￥ {{ summary.total_income }}</h5>
        </div>
        <div class="col">
          <h5 class="text-center text-danger">￥ {{ summary.total_expense }}</h5>
        </div>
      </div>
    </div>
    <hr class="mt-3 mb-3" style="border: 0; border-top: 2px solid #FFC107;"/>
    <div id="payment-methods">
      <ul class="list-group">
        <li class="list-group-item" v-for="payment in paymentDetail" :key="payment.name">
          <div class="form-row">
            <div class="col-md-6">
              <font-awesome-icon
                :icon="['far', 'money-bill-alt']"
                class="icon alt mr-1"
              />
              {{ payment.name }}
            </div>
            <div class="col-md-6 text-right">
              <div v-if="payment.amount < 0" class="text-danger">
                {{ payment.amount }}
              </div>
              <div v-else class="text-success">
                {{ payment.amount }}
              </div>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script lang="ts">
import { mapGetters, mapActions } from "vuex"
import { Options, Vue } from "vue-class-component";


@Options({
  name: "BillSummary",
  data() {
    return {
    }
  },
  computed: {
    getCurrentDate() {
      const date = new Date()
      return `${date.getFullYear()} / ${date.getMonth() + 1}`
    },
    ...mapGetters({
      summary: "bill/summary",
      paymentDetail: "bill/paymentDetail",
      billId: "bill/billId"
    })
  },
  watch: {
    billId: function() {
      this.getBillSummary()
    }
  },
  methods: {
    ...mapActions({
      getBillSummary: "bill/getBillSummary"
    })
  },
  mounted: async function mounted () {
    await this.getBillSummary()
  },
})
export default class Home extends Vue {}
</script>
