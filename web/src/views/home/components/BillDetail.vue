<template>
  <div id="bill" class="container">
    <div class="card mb-4" v-for="bill in bills" :key="bill.created_at">
      <div class="card-header">{{ $filters.dateFormat(bill.created_at) }} </div>
      <div class="card-body">
        <div class="form-row">
          <div class="col-md-6">
            <h5>
              {{ bill.usage.name }}
            </h5>
            <small class="form-text text-muted">{{ bill.note }}</small>
          </div>
          <div class="col-md-6 text-right">
            <h5 class="text-danger" v-if="bill.bill_type == 'expense'">
              - {{ bill.price }}
            </h5>
            <h5 class="text-success" v-else>+ {{ bill.price }}</h5>
            <small class="form-text text-muted">{{ bill.payment.name }}</small>
          </div>
        </div>
      </div>
    </div>
    <div class="mt-3 mb-3">
      <nav v-if="pagination.total_pages > 1">
        <div class="pagination justify-content-center">
          <paginate
            :page-count="pagination.total_pages"
            :click-handler="paginationClickHandler"
          >
          </paginate>
        </div>
      </nav>
    </div>
  </div>
</template>

<script lang="ts">
import { mapGetters, mapActions } from "vuex";
import { Options, Vue } from "vue-class-component";

import VPagination from "vue3-pagination";
import "vue3-pagination/dist/vue3-pagination.css";

@Options({
  name: "BillDetail",
  components: {
    VPagination
  },
  data() {
    return {
      page: 1,
    };
  },
  computed: {
    ...mapGetters({
      bills: "bill/bills",
      billId: "bill/billId",
      pagination: "bill/pagination",
    }),
  },
  watch: {
    billId: function () {
      this.getFitstPageBillDetails();
    },
  },
  methods: {
    getFitstPageBillDetails() {
      const payload = {
        page: 1,
      };
      this.getBills(payload);
    },
    paginationClickHandler(page: number) {
      const payload = {
        page,
      };
      this.getBills(payload);
    },
    ...mapActions({
      getBills: "bill/getBills",
      initState: "bill/initState",
    }),
  },
  mounted: async function mounted() {
    this.initState();
    await this.getFitstPageBillDetails();
  },
})
export default class Home extends Vue {}
</script>
