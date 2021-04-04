import OpenAPIClientAxios from 'openapi-client-axios'
import axios from 'axios'

const BASE_URL: string = process.env.VUE_APP_API_DOMAIN

async function getOpenApi() {
    let openApi = ''
    await axios.get(`${BASE_URL}/bill/openapi.json`)
    .then(function (response) {
        openApi = JSON.stringify(response.data)
        localStorage.setItem(`bookkeeping-openapi`, openApi)
    })
    .catch(function (error) {
        console.log(`Failed to download OpenAPI file, error: ${error}`)
    })
    return openApi
}


async function getAPI() {
    let apiClient = null
    let cli = null
    try {
        let openApiSpec: string = localStorage.getItem(`bookkeeping-openapi`) || ''
        if (!openApiSpec) {
            openApiSpec = await getOpenApi()
        }
        openApiSpec = JSON.parse(openApiSpec)
        apiClient = new OpenAPIClientAxios({
            definition: openApiSpec,
            axiosConfigDefaults: {
                baseURL: BASE_URL
            }
        })
        apiClient.init()
        cli = await apiClient.getClient()
    } catch (error) {
        console.log(`Fail to init OpenAPI client, error: ${error}`)
        return null
    }
    return cli
}

export {
    getAPI
}