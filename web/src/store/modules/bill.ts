import billService from '@/service/bill-service'
import { getField, updateField } from 'vuex-map-fields'

type BillDetail = {
    'payment': any,
    'bill_type': string,
    'usage': any,
    'currency': any,
    'price': number,
    'note': string,
    'updated_at': string,
}

type Pagination = {
    'count': number,
    'next': string | null,
    'previous': string | null,
    'total_pages': number
}

type BillSummary = {
    'total_expense': number,
    'total_income': number
}

type Payment = {
    'name': string,
    'amount': number
}

type BillInfo = {
    'payment': any[],
    'usage': any[],
    'currency': any[],
    'bill_type': string[]
}

type BillForm = {
    'payment': string,
    'billType': string,
    'usage': string,
    'currency': string,
    'price': number,
    'note': string
}

function isEmptyObject(obj: any) {
    return Object.keys(obj).length === 0
}

function getBillFormRequestData(billForm: BillForm) {
    console.log(billForm)
    return {
        "payment_id": billForm.payment,
        "bill_type": billForm.billType,
        "usage_id": billForm.usage,
        "currency_id": billForm.currency,
        "price": billForm.price,
        "note": billForm.note
      }
}

const getters = {
    bills: (state: any) => {
        return state.bills
    },
    pagination: (state: any) => {
        return state.pagination
    },
    summary: (state: any) => {
        return state.summary
    },
    paymentDetail: (state: any) => {
        return state.paymentDetail
    },
    billInfo: (state: any) => {
        return state.billInfo
    },
    getAddBillFormField(state: any) {
        return getField(state.addBillForm)
    },
    addBillFormErrors: (state: any) => {
        return state.addBillFormErrors
    },
    billId:  (state: any) => {
        return state.billId
    }
}

const actions = {
    initState(context: any) {
        Object.assign(context.state, initialState())
    },
    async getBills(context: any, payload: any) {
        const resp = await billService.getBills(payload)
        context.commit('setBills', resp.items)
        context.commit('setPagination', resp.pagination)
    },
    async getBillSummary(context: any) {
        const resp = await billService.getBillSummary()
        context.commit('setSummary', resp.summary)
        context.commit('setPaymentDetail', resp.payment_detail)
    },
    async getBillInfo(context: any) {
        const resp = await billService.getBillInfo()
        context.commit('setBillInfo', resp)
    },
    async addBill(context: any) {
        // do validation
        context.dispatch('bill/_validate_form', null, { root: true })

        // terminate if any form error exists
        const commonFormErrors = context.getters.addBillFormErrors
        if (!isEmptyObject(commonFormErrors)) {
            throw new Error('Add bill form is invalid')
        }

        const billFormData = context.state.addBillForm
        const resp = await billService.addBill(getBillFormRequestData(billFormData))
        context.commit('setBillId', resp.id)
    },
    _validate_form(context: any) {
        const errors: any = {}

        if (!context.state.addBillForm.payment.length) {
            errors.payment = true
        }

        if (!context.state.addBillForm.billType.length) {
            errors.billType = true
        }

        if (!context.state.addBillForm.usage.length) {
            errors.usage = true
        }

        if (!context.state.addBillForm.currency.length) {
            errors.currency = true
        }

        if (!context.state.addBillForm.price.toString().length || parseInt(context.state.addBillForm.price) < 0) {
            errors.price = true
        }

        context.commit('setFormErrors', errors)
    }
}

const mutations = {
    setBills(state: any, bills: BillDetail[]) {
        state.bills = bills
    },
    setPagination(state: any, pagination: Pagination) {
        state.pagination = pagination
    },
    setSummary(state: any, summary: BillSummary) {
        state.summary = summary
    },
    setPaymentDetail(state: any, paymentDetail: Payment[]) {
        state.paymentDetail = paymentDetail
    },
    setBillInfo(state: any, billInfo: BillInfo) {
        // set billInfo
        state.billInfo.payment = billInfo.payment
        state.billInfo.billType = billInfo.bill_type
        state.billInfo.usage = billInfo.usage
        state.billInfo.currency = billInfo.currency
        // set bill form default value
        state.addBillForm.payment = billInfo.payment[0].id
        state.addBillForm.billType = billInfo.bill_type[1]
        state.addBillForm.usage = billInfo.usage[0].id
        state.addBillForm.currency = billInfo.currency[0].id
    },
    updateAddBillFormField(state: any, field: any) {
        updateField(state.addBillForm, field);
    },
    setFormErrors(state: any, addBillFormErrors: any) {
        state.addBillFormErrors = addBillFormErrors
    },
    setBillId(state: any, billId: number) {
        state.billId = billId
    },
}

function initialState() {
    return {
        billId: 0,
        bills: [],
        pagination: {
            total_number_of_items: 0,
            current_page: 1,
            next_page: null,
            previous_page: null,
            total_pages: 0
        },
        summary: {
            total_expense: 0,
            total_income: 0
        },
        paymentDetail: [],
        billInfo: {
            payment: [],
            usage: [],
            currency: [],
            billType: []
        },
        addBillForm: {
            payment: '',
            billType: '',
            usage: '',
            currency: '',
            price: 0,
            note: ''
        },
        addBillFormErrors: {}
    }
}

export default {
    namespaced: true,
    actions,
    getters,
    mutations,
    state: initialState()
}
