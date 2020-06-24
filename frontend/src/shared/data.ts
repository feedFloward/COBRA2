import Axios, * as axios from 'axios';

const baseUrl : string = "http://127.0.0.1:8000";

const trainRequest = async function(data: Object) {
    Axios.defaults.xsrfCookieName = 'csrftoken';
    Axios.defaults.xsrfHeaderName = 'X-CSRFToken';
    const response = await axios.default.post(baseUrl+'/train', JSON.stringify(
        {
            data: data
        }
    ))
    return response.data
};

export const data = {
    trainRequest,
};