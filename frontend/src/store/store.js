import { configureStore } from '@reduxjs/toolkit';

import loginSlice from './features/auth/loginSlice';
import hotelReducer from './features/hotel/hotelSlice';


const store = configureStore({
    reducer: {
        hotels: hotelReducer,
        user: loginSlice
    }
});

export default store;