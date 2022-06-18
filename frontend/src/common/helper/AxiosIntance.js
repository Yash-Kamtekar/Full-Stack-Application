import axios from "axios";

const axiosInstance = axios.create({ baseURL: `http://127.0.0.1:8000/` });

axiosInstance.interceptors.request.use((config) => {

    // config.params = config.params || "";
    // config.params["auth"] = "test";

    return config;
})

export default axiosInstance;