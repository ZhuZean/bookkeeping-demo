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
  const res = await client!.listBills(page)
  return res.data
}

async function getBillSummary() {
  await initClient()
  const client = await getAPI()
  const res = await client!.listBillSummarys()
  return res.data
}

async function getBillInfo() {
  await initClient()
  const client = await getAPI()
  const res = await client!.listBillInfos()
  return res.data
}

async function addBill(data: any) {
  await initClient()
  const client = await getAPI()
  const res = await client!.createBill(undefined, data)
  return res.data
}

export default {
  getBills,
  getBillSummary,
  destroyClient,
  getBillInfo,
  addBill
}
