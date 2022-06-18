import React, { useEffect } from "react";

import { useDispatch, useSelector } from "react-redux";
import { fetchHotels } from "../../store/features/hotelSlice";

function Hotel() {
    const hotels = useSelector(state => state.hotels);
    const disptach = useDispatch();

    useEffect(() => {
        disptach(fetchHotels());
    }, [])

    function addHotel() {
        // props.addHotel();
    }

    return (
        <div className="container-md">
            <div className="row">
                {hotels["hotels"] !== undefined && hotels.hotels.map((item, id) => (
                    <div key={id} className="col-md-3">
                        {item.hotel_name}
                        {item.address}
                    </div>
                ))}

                <button className="btn btn-primary" onClick={() => addHotel()}>
                    Add Hotel
                </button>
            </div>
        </div>
    )
}


export default Hotel;