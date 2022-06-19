import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";

import { axiosInstance } from "../../../common";

const initialState = {
    loading: false,
    hotels: [],
    error: ""
};

export const fetchHotels = createAsyncThunk("hotel/fetchHotels", () => {
    return axiosInstance.get("hotels/").then(res => res.data);
});


const hotelSlice = createSlice({
    name: "hotel",
    initialState,
    extraReducers: builder => {
        builder.addCase(fetchHotels.pending, state => {
            state.loading = true
        })
        builder.addCase(fetchHotels.fulfilled, (state, action) => {
            state.loading = false
            state.hotels = action.payload
            state.error = ""
        })
        builder.addCase(fetchHotels.rejected, state => {
            state.loading = false
            state.hotels = []
            state.error = "error"
        })
    }
})

export default hotelSlice.reducer;