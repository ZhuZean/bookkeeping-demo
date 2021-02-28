<template>
  <div id="record" class="container">
    <form>
      <div class="row">
        <div class="col">
          <select class="form-control" v-model="payment">
            <option
              v-for="(paymentName, index) in billInfo.payment"
              :key="index"
              v-bind:value="paymentName"
            >
              {{ paymentName }}
            </option>
          </select>
        </div>
        <div class="col">
          <select class="form-control" v-model="billType">
            <option
              v-for="(billTypeName, index) in billInfo.billType"
              :key="index"
              v-bind:value="billTypeName"
            >
              {{ billTypeName }}
            </option>
          </select>
        </div>
        <div class="col">
          <select class="form-control" v-model="usage">
            <option
              v-for="(usageName, index) in billInfo.usage"
              :key="index"
              v-bind:value="usageName"
            >
              {{ usageName }}
            </option>
          </select>
        </div>
      </div>
      <div class="row mt-3">
        <div class="col-4">
          <select class="form-control" v-model="currency">
            <option
              v-for="(currencyName, index) in billInfo.currency"
              :key="index"
              v-bind:value="currencyName"
            >
              {{ currencyName }}
            </option>
          </select>
        </div>
        <div class="col">
          <input
            type="number"
            min="0"
            class="form-control"
            placeholder=""
            v-model="price"
            v-bind:class="{ 'is-invalid': addBillFormErrors.price }"
          />
          <div class="invalid-feedback">{{ $t("Home.AddRecord.form.price.error") }}</div>
        </div>
      </div>
      <div class="form row mt-3">
        <div class="col">
          <label for="notes"> {{ $t("Home.AddRecord.form.notes.label") }}</label>
          <input
            type="text"
            class="form-control"
            id="notes"
            placeholder="note"
            v-model="note"
          />
        </div>
      </div>
      <div class="text-right mt-4">
        <button type="button" class="btn btn-primary" @click="addBill()">
          {{ $t("Home.AddRecord.form.submit_btn") }}
        </button>
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import { mapGetters, mapActions } from "vuex";
import { Options, Vue } from "vue-class-component";
import { createHelpers } from "vuex-map-fields";

const { mapFields } = createHelpers({
  getterType: "bill/getAddBillFormField",
  mutationType: "bill/updateAddBillFormField",
});

@Options({
  name: "AddRecord",
  data() {
    return {};
  },
  computed: {
    ...mapGetters({
      billInfo: "bill/billInfo",
      addBillForm: "bill/addBillForm",
      addBillFormErrors: "bill/addBillFormErrors",
      billId: 'bill/billId'
    }),
    ...mapFields({
      payment: "payment",
      billType: "billType",
      usage: "usage",
      currency: "currency",
      price: "price",
      note: "note",
    }),
  },
  watch: {
    billId: function() {
      this.price = 0
      this.note = ''
    }
  },
  methods: {
    ...mapActions({
      getBillInfo: "bill/getBillInfo",
      addBill: "bill/addBill",
    }),
  },
  mounted: async function mounted() {
    await this.getBillInfo();
  },
})
export default class Home extends Vue {}
</script>
