import axios from "axios";


export function getHotels() {
    return axios.get("http://127.0.0.1:8000/hotels/");
}

export function formatHotels(hotelsData) {
    let hotels = [];

    return hotels;
}