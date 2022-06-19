import React, { lazy, Suspense, useEffect } from "react";

import { Route, Routes } from 'react-router-dom';

import { NavBar } from "./common";

const LazyLogin = lazy(() => import("./pages/auth/login"));
const LazyHotel = lazy(() => import("./pages/hotel/index"));


function App() {

    let token = "";

    useEffect(() => {
        token = localStorage.getItem("token");
    }, []);


    let routes = (
        <Routes>
            <Route path="/login" element={<LazyLogin />} />
            <Route path="*" element={<LazyLogin />} />
        </Routes>
    );

    if (!["", NaN, null, undefined, false].includes(token)) {
        routes = (
            <Suspense fallback={<div>..loading</div>}>
                <Route path="/app" element={<LazyHotel />} />
                <Route path="*" element={<LazyHotel />} />
            </Suspense>
        );
    }

    return (
        <>
            {/* <NavBar /> */}
            <Suspense fallback={<div>..loading</div>}>
                {routes}
            </Suspense>
        </>
    );
}

export default App;
