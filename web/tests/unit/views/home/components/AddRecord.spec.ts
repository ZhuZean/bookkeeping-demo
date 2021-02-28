// @ts-nocheck
import { shallowMount } from '@vue/test-utils'
import { createStore } from 'vuex'

import Vuex from 'vuex'

import localization from '../../../mocks/localization.mock'
import AddRecord from '@/views/home/components/AddRecord.vue'
import bill from '@/store/modules/bill'
import store from '@/store'


describe('Home.vue', () => {
  let store: any
  let components: any

  beforeEach(() => {
    store = createStore({
      modules: {
        bill
      }
    })

    components = {
      plugins: [store],
      mocks: {
        ...localization
      },
    }
  })

  it('can render', () => {
    const wrapper = shallowMount(AddRecord, {
      global: components
    })
    expect(wrapper.element).toMatchSnapshot()
  })

  it('can watch billId', async () => {
    const wrapper = shallowMount(AddRecord, {
      global: components
    })
    // set the value of price and note
    wrapper.vm.price = 1000
    wrapper.vm.note = 'test'

    // commit to change the value of billId
    store.commit('bill/setBillId', 'new-id')
    await wrapper.vm.$nextTick()

    // watch the change of BillId and reset the value of billId
    expect(wrapper.vm.price).toBe(0)
    expect(wrapper.vm.note).toBe('')
    expect(wrapper.element).toMatchSnapshot()
  })

})
