import React, { useState } from "react";
import { NavLink } from "react-router-dom";

import { Elements } from "../../common";


const Login = () => {

    const [val, setVal] = useState({
        username: "",
        password: ""
    })
    const [loading, setLoading] = useState(false);

    function onchange(newval, id) {
        let temp = { ...val }
        temp[id] = newval
        setVal(temp)
    }

    function login(e) {
        e.preventDefault();


    }

    return (
        <div className='container d-flex flex-row justify-content-center align-items-center' style={{ height: '100vh' }}>
            <div className='card col-5 shadow p-3' id='login_container'>
                <form onSubmit={(e) => login(e)}>
                    <h1 className='d-flex flex-row justify-content-center mb-4 fw-normal'> Log in</h1>
                    <div className='row justify-content-center'>
                        <Elements
                            formField={[
                                {
                                    id: 'username',
                                    label: 'Username *',
                                    type: 'text',
                                    placeholder: 'Enter Username',
                                    className: 'col-7',
                                    autoFocus: true,
                                    requiredFlag: true,
                                    value: val.username,
                                    onchange: onchange,
                                },
                                {
                                    id: 'password',
                                    label: 'Password *',
                                    type: 'password',
                                    placeholder: 'Enter Password',
                                    className: 'col-7',
                                    requiredFlag: true,
                                    value: val.password,
                                    onchange: onchange
                                },
                            ]}
                        />
                    </div>
                    {/* {loginError !== null && <p>
                        <font color='red'>{loginError}</font>
                    </p>} */}
                    <div className='d-flex justify-content-center'>
                        {/* <Button
                            text='Login'
                            type='submit'
                            loading={loading}
                        /> */}
                    </div>
                </form>
                <div className='d-flex justify-content-center pt-3 pb-3' style={{ color: '#666666' }}>
                    <p className='mb-0'>
                        Don't have an account?
                    </p>
                    <NavLink to='/register' className='text-primary ms-2'>
                        Register
                    </NavLink>

                </div>
            </div>
        </div>
    )
}

export default Login;