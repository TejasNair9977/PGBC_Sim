import cover from "../../assets/bg.svg"

const RegisterWrapper = (props)=>{
    return(
        <>
            
            <div style={{height:"100%",width:"100%",display:"flex",alignItems:"center", justifyContent:"center",backgroundImage:`url(${cover})`}}>
                    
                        {props.children}
                    
            </div>
            
        </>
    )
}

export default RegisterWrapper