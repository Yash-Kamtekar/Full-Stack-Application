import React from "react";
import { NavLink } from "react-router-dom";


export const NavBar = () => {

    return (
        <nav className="navbar fixed-top navbar-dark bg-dark">
            <div className="container-fluid">
                <NavLink
                    to="/"
                    className=""
                >
                    Data Marvels
                </NavLink>

                <NavLink
                    to="/login"
                    className=""
                >
                    Register/Login
                </NavLink>

            </div>
        </nav>

    )
}