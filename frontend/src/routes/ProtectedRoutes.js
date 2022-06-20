import React from "react";
import { Navigate, Outlet } from "react-router-dom";


const ProtectedRoutes = () => {
    const isAuthenticated = localStorage.getItem("token");

    return (
        <>
            {![undefined, NaN, null, false, 0, ""].includes(isAuthenticated) ? <Outlet /> : <Navigate to="/login" />}
        </>
    )
}

export default ProtectedRoutes;