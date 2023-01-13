import './register.css';
import { Link, useNavigate } from 'react-router-dom';
import Axios from 'axios';
import React, { useState } from 'react';
function RegisterUi() {
  const navigate = useNavigate();
  const url="http://127.0.0.1:5000/create"
    const [user, setUser]=useState({Cemail:"",username:"",Cpassword:""});
   function handleInputs(e){
   const newdata={...user}
   newdata[e.target.id]=e.target.value;
   setUser(newdata)
   //console.log(newdata)

  }
  function submt(e){
    e.preventDefault();
    Axios.post(url,{Cemail:user.Cemail,username:user.username,Cpassword:user.Cpassword})
    .then((res)=>{
      if(res.data=='Account created'){
        // debugger
        navigate("/add_attn");};
      /*e.target.reset();*/}
    )
    .catch((error)=>{console.log(error)})
    }
  return (
    <div className="main">
     <div className="sub-main">
       <div>     
         <div>
           <h1>Registration </h1>
           <div>     
             <input type="email" id="Cemail"   onChange={(e)=>handleInputs(e)} value={user.Cemail} placeholder="email" className="name"/>
           </div>
           <div className="second-input">
           
             <input type="text" id="username"  onChange={(e)=>handleInputs(e)} value={user.username} placeholder="username" className="name"/>
           </div>
           <div className="third-input">           
           <input type="password" id="Cpassword"  onChange={(e)=>handleInputs(e)} value={user.Cpassword} placeholder="password" className="name"/>
         </div>
          <div className="login-button">
          <button id='done'  onClick={(e)=>submt(e)}>Register</button>
          </div>
            {/* <p className="link">
              <a href="#">Forgot password ?</a> Or <a href="#"> Sign Up</a>
            </p> */}
         </div>
       </div>
     </div>
    </div>
  );
}

export default RegisterUi;