import React, { lazy, Suspense } from "react";

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import { NavBar } from "../common";
import ProtectedRoutes from "./ProtectedRoutes";
import UnProtectedRoutes from "./UnProtectedRoutes";

const LazyLogin = lazy(() => import("../pages/auth/login"));
const LazyHotel = lazy(() => import("../pages/hotel/index"));


function Webpage() {
    return (
        <>
            {/* <NavBar /> */}
            <Router>
                <Suspense fallback={<div>..loading</div>}>
                    <Routes>
                        <Route element={<ProtectedRoutes />}>
                            <Route element={<LazyHotel />} path="/app" />
                        </Route>
                        <Route element={<UnProtectedRoutes />}>
                            <Route element={<LazyLogin />} path="/login" />
                        </Route>
                    </Routes>
                </Suspense>
            </Router>
        </>
    );
}

export default Webpage;
