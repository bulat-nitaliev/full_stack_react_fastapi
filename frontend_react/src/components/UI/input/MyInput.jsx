import cl from './MyInput.module.css'

const Myinput = (props)=>{
    return (
        <div>
            <input className={cl.inp} {...props} />
        </div>
    )
}
export default Myinput