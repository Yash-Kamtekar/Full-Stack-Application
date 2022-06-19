import React, { lazy, Suspense } from "react";

import { Route, Routes } from 'react-router-dom';

import { NavBar } from "./common";

const LazyLogin = lazy(() => import("./pages/auth/login"));
const LazyHotel = lazy(() => import("./pages/error"));
const LazyNoMatch = lazy(() => import("./pages/hotel"));


function App() {

    return (
        <>
            {/* <NavBar /> */}
            <Suspense fallback={<div>..loading</div>}>
                <Routes>
                    {/* <Routes> */}
                    <Route path="/app" element={<LazyHotel />} />
                    <Route path="/login" element={<LazyLogin />} />
                    <Route path="*" element={<LazyNoMatch />} />
                    {/* </Routes> */}
                </Routes>
            </Suspense>
        </>
    );
}

export default App;
