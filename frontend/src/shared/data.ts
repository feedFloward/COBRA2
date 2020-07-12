import Axios, * as axios from 'axios';
import {clfObject} from '@/types/classification'

const baseUrl : string = "http://127.0.0.1:8000";

const trainRequest = async function(data: Object, inputspace: [number, number], model: clfObject) {
    Axios.defaults.xsrfCookieName = 'csrftoken';
    Axios.defaults.xsrfHeaderName = 'X-CSRFToken';
    const response = await axios.default.post(baseUrl+'/train', JSON.stringify(
        {
            data: data,
            inputspace: inputspace,
            model: model
        }
    )).catch(error => {
        throw new Error(`COBRA api service ${error}`)
    })
    return response.data
};

export const data = {
    trainRequest,
};