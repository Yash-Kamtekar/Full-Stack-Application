import { applyMiddleware, compose, createStore } from "redux";
import HotelReducer from "./reducer/HotelReducer";
import thunk from "redux-thunk";


const middleware = applyMiddleware(thunk);

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
// const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__();


export const store = createStore(HotelReducer, composeEnhancers(middleware));