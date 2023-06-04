import axios from "axios";

export const getData = async (URL) => {
    try {
        const {data} = await axios.get(URL)
        return data
    } catch (e) {
        alert(e)
    }
}

export const postData = async (URL, payload) => {
    const headers = {
        'Content-Type': 'application/json',
    }
    try {
        const data = await axios.post(URL, payload, {headers:headers})
        alert("Created")
        return data
    } catch (error) {
        alert(Object.keys(error.response.data).reduce((acc, el) => {
            return acc + error.response.data[el][0] + '\n'
        }, ''))

    }
}

export const patchData = async (URL, payload) => {
    const headers = {
        'Content-Type': 'application/json',
    }
    try {
        const data = await axios.patch(URL, payload, {headers:headers})
        alert("success, refresh the page")
        return data
    } catch (error) {
        alert(Object.keys(error.response.data).reduce((acc, el) => {
            return acc + error.response.data[el][0] + '\n'
        }, ''))

    }
}

export const deleteData = async (URL) => {
    try {
        const data = await axios.delete(URL)
        return data
    } catch (error) {
        alert(Object.keys(error.response.data).reduce((acc, el) => {
            return acc + error.response.data[el][0] + '\n'
        }, ''))

    }
}
