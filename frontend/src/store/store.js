import { configureStore } from '@reduxjs/toolkit';

import hotelReducer from './features/hotelSlice';


const store = configureStore({
    reducer: {
        hotels: hotelReducer
    }
});

export default store;