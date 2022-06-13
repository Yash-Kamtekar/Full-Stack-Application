import { ADD_HOTEL_ACTION, CONFIRMED_GET_HOTELS_ACTION } from "../actions/HotelAction";


const initialState = {
    hotels: []
}

export default function HotelReducer(state = initialState, actions) {

    switch (actions.type) {
        case ADD_HOTEL_ACTION:

            let hotels = [];

            return state = {
                ...state,
                hotels
            }

        case CONFIRMED_GET_HOTELS_ACTION:

            return {
                ...state,
                hotels: actions.payload
            }


        default:
            state = { ...state }
    }
    return state;

}