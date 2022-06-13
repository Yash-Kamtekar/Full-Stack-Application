import React, { useEffect } from "react";
import { connect } from "react-redux";
import { addHotelAction, getHotelAction } from "../../store/actions/HotelAction";


function Hotel(props) {

    useEffect(() => {
        props.getHotel();
    }, [])

    function addHotel() {
        props.addHotel();
    }

    return (
        <div className="container-md">
            <div className="row">
                {props.hotels.map((item, id) => (
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

const mapStateToProps = (state) => {
    return {
        hotels: state.hotels
    }
}

const mapDisptachToProps = (dispatch) => {
    return {
        addHotel: () => dispatch(addHotelAction()),
        getHotel: () => dispatch(getHotelAction())
    }
}

export default connect(mapStateToProps, mapDisptachToProps)(Hotel);