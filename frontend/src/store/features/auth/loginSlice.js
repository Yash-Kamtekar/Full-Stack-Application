import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";

import { axiosInstance } from "../../../common";


const initialState = {
    loading: false,
    user: {},
    token: "",
    error: ""
};


export const loginUser = createAsyncThunk("user/login", (bodyData) => {
    let body = {
        grant_type: "",
        username: bodyData.username,
        password: bodyData.password,
        scope: "",
        client_id: "",
        client_secret: ""
    };

    return axiosInstance.post("login", new URLSearchParams(body)).then(res => res.data);
});

const loginSlice = createSlice({
    name: "login",
    initialState,
    extraReducers: builder => {
        builder.addCase(loginUser.pending, state => {
            state.loading = true
        })
        builder.addCase(loginUser.fulfilled, (state, action) => {
            state.loading = false
            state.user = action.payload.user_details
            state.token = action.payload.access_token
            state.error = ""

            localStorage.setItem("token", action.payload.access_token);
        })
        builder.addCase(loginUser.rejected, (state, action) => {
            state.loading = false
            state.user = {}
            state.token = ""
            state.error = action.error.message
        })
    }
})

export default loginSlice.reducer;