import { shallowMount } from '@vue/test-utils'
import Home from '@/views/home/Home.vue'

describe('Home.vue', () => {
  it('can render', () => {
    const wrapper = shallowMount(Home)
    expect(wrapper.element).toMatchSnapshot()
  })
})
