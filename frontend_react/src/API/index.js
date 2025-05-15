import axios from "axios";

export default class AuthService {
    static async login({ email, password }) {
        const response = await axios.post("http://localhost:8000/auth/login", {
            email,
            password,
        });
        return response;
    }

 
}
