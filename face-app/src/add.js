import './add.css';
import { Link } from 'react-router-dom';
import Axios from 'axios';
import React, { useState } from 'react';
function AddUi() {
  const url="http://127.0.0.1:5000/add"
  const [success, setSuccess]=useState("");
    const [user, setUser]=useState({namey:""});
   function handleInputs(e){
   const newdata={...user}
   newdata[e.target.id]=e.target.value;
   setUser(newdata)
   console.log(newdata)

  }
  function submt(e){
    e.preventDefault();
    Axios.post(url,{namey:user.namey})
    .then((res)=>{console.log(res);
      /*e.target.reset();*/}
    )
    .catch((error)=>{console.log(error)})
    }

    const url2="http://127.0.0.1:5000/atten"
    function submt2(e){
        e.preventDefault();
        Axios.get(url2)
        .then((res)=>{
          setSuccess("done");
          setTimeout(() => {
            setSuccess("")
          }, 3000);

          /*e.target.reset();*/}
        )
        .catch((error)=>{console.log(error)})
        }
  return (
    <div className="main">
     <div className="sub-main">
     
       <div>     
         <div>
           <h1>Enter Name Of Student </h1>
           
           <div className="second-input">
           
           <input type="text" id="namey"   onChange={(e)=>handleInputs(e)} value={user.namey} placeholder="Student's name" className="name"/>
         </div>
          
          <div className="login-button">
          <button id='done'  onClick={(e)=>submt(e)}>Add Student</button>  </div>
          <div className="takeattn-button">
          <button onClick={(e)=>submt2(e)} className="li" >Take Attendance</button>
          </div>
          <div className="adddata-button">
          <button><a href='http://127.0.0.1:5000/getdata'>See Attendance</a></button>
          </div>
          <div className="adddata-button">
          <button><Link className='li' to='/'>Log Out</Link></button>
          </div>
          <h3 className='success'>{success}</h3>
         
        
            {/* <p className="link">
              <a href="#">Forgot password ?</a> Or <a href="#"> Sign Up</a>
            </p> */}
         </div>
       </div>
     </div>
    </div>
  );
}

export default AddUi;