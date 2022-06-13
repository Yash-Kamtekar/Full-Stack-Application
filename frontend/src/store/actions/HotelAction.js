import { formatHotels, getHotels } from "../../services/HotelService";

export const ADD_HOTEL_ACTION = "Add Hotel";
export const GET_HOTEL_ACTION = "Get Hote";
export const CONFIRMED_GET_HOTELS_ACTION = "Confirmed Get Hotels";


export function addHotelAction() {

    return {

        type: ADD_HOTEL_ACTION

    }

}

export function getHotelAction() {

    return (dispatch) => {

        getHotels().then((res) => {
            let hotels = formatHotels(res.data);
            dispatch(confirmedGetHotelAction(hotels));
        })
    };

}


export function confirmedGetHotelAction(hotels) {

    return {

        type: CONFIRMED_GET_HOTELS_ACTION,
        payload: hotels

    }

}