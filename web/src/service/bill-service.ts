import { getAPI } from '@/service/common'

let client:any = null

async function initClient() {
  if (client === null) {
    client = await getAPI()
  }
}

function destroyClient() {
  client = null
}

async function getBills(payload: any) {
  await initClient()
  const client = await getAPI()
  const page: number = payload.page
  const res = await client!.list_bills_bill_get(page)
  return res.data
}

async function getBillSummary() {
  await initClient()
  const client = await getAPI()
  const res = await client!.summary_bill_summary_get()
  return res.data
}

async function getBillInfo() {
  await initClient()
  const client = await getAPI()
  const res = await client!.form_info_bill_form_info_get()
  return res.data
}

async function addBill(data: any) {
  await initClient()
  const client = await getAPI()
  const res = await client!.create_bill_post(undefined, data)
  return res.data
}

export default {
  getBills,
  getBillSummary,
  destroyClient,
  getBillInfo,
  addBill
}
