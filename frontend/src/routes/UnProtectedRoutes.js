import React from "react";
import { Navigate, Outlet } from "react-router-dom";


const UnProtectedRoutes = () => {
    const isAuthenticated = localStorage.getItem("token");

    return (
        <>
            {![undefined, NaN, null, false, 0, ""].includes(isAuthenticated) ? <Navigate to="/app" /> :  <Outlet />}
        </>
    )
}

export default UnProtectedRoutes;