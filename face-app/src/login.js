import './login.css';
import { Link, useNavigate } from 'react-router-dom';
import Axios from 'axios';
import React, { useState } from 'react';
import AppUi from './App';
function LoginUi() {
  const navigate = useNavigate();
  
const url="http://127.0.0.1:5000/login"
    const [user, setUser]=useState({Lemail:"",username:"",Lpassword:""});
   function handleInputs(e){
   const newdata={...user}
   newdata[e.target.id]=e.target.value;
   setUser(newdata)
  }
  function submt(e){
    e.preventDefault();
    // debugger
    Axios.post(url,{Lemail:user.Lemail,username:user.username,Lpassword:user.Lpassword})
    .then((res)=>{
      if(res.data=='Logged-in'){
        // debugger
        navigate("/add_attn");}
      /*e.target.reset();*/}
    )
    .catch((error)=>{console.log(error)})
    }
  return (
    <div className="main">
     <div className="sub-main">
       <div>   
         <div>
           <h1>Login</h1>
           <div>
             <input type="email" id="Lemail"   onChange={(e)=>handleInputs(e)} value={user.Lemail} placeholder="email" className="name"/>
           </div>
           <div className="second-input">
           <input type="text" id="username"  onChange={(e)=>handleInputs(e)} value={user.username}  placeholder="username" className="name"/>
           </div>
           <div className="third-input">
           <input type="password" id="Lpassword"  onChange={(e)=>handleInputs(e)} value={user.Lpassword} placeholder="password" className="name"/>
           </div>
          <div className="login-button">
          <button id='done'  onClick={(e)=>submt(e)}>Sign-In</button>
          </div> 
            <p className="link">
              <Link to="/register"> Sign Up</Link>
            </p>
        </div>
       </div>    
     </div>
    </div>
  );
}

export default LoginUi;