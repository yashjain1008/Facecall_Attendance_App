import './add_attn.css';
import Axios from 'axios';
import { Link } from 'react-router-dom';
import SuccessPopup from 'react-success-popup';
import { useState } from 'react';


function Add_attnUi() {
    const url="http://127.0.0.1:5000/atten"
    const [success, setSuccess]=useState("");
        function submt(e){
            e.preventDefault();
            Axios.get(url)
            .then((res)=>{
        
              setSuccess("done")
              /*e.target.reset();*/}
            )
            .catch((error)=>{console.log(error)})
            }
  return (
    <>
  
    
    <div className="main">
     
     <div className="sub-main">
     
       <div>
         
         <div>
           <h1>Welcome</h1>
          
          <div className="adddata-button">
          <button><Link className='li' to='/add'>Add Student Data</Link></button>
          </div>
          <div className="takeattn-button">
          <button onClick={(e)=>submt(e)} className="li" >Take Attendance</button>
          </div>
          <div className="adddata-button">
          <button><a href='http://127.0.0.1:5000/getdata'>See Attendance</a></button>
          </div>
          <div className="adddata-button">
          <button><Link className='li' to='/'>Log Out</Link></button>
          </div>
        
          
 
         </div>
       </div>
       

     </div>
    </div>
    </>
  );
}

export default Add_attnUi;