import { React, useState } from "react"
import MyButton from "./UI/button/MyButton"
import Myinput from "./UI/input/MyInput"
import AuthService from "../API"

const FormLogin = ()=>{
    const [loginData, setLoginData] = useState({"email":"", "password":""})
    const login = async (e)=>{
        e.preventDefault()
        try {
            const response = await AuthService.login(loginData)
            const res = response.data
            localStorage.setItem("access_token",res.access_token)
            setLoginData({"email":"", "password":""})
        } catch (error) {
            console.log(error);
            
        }
        
        
    }

    return (
        <form onSubmit={login} style={{marginTop:50}}>
            <h2>войти на сайт</h2>
            <Myinput 
            type="email" 
            placeholder="Введите емайл" 
            value={loginData.email}
            onChange={(e)=> setLoginData({...loginData, email:e.target.value})}
            />
            <Myinput 
            type="password"
            placeholder="Введите пароль" 
            value={loginData.password}
            onChange={(e)=> setLoginData({...loginData, password:e.target.value})}
            />
            <MyButton>Войти</MyButton>
        </form>
    )
}

export default FormLogin