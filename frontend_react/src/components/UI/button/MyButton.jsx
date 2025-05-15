import cl from "./MyButton.module.css"

const MyButton = ({children, ...props})=>{
    return (
        <div>
            <button {...props} className={cl.myBtn} >{children}</button>
        </div>
    )
}

export default MyButton