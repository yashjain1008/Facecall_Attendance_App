import { render } from "@testing-library/react";
import axios from "axios";
import React,{useState,useEffect} from "react";


// export default see;
function teeUi() {
    const [nm, setdt]=useState(false)
    function getdt(){
        setdt(val.tareget.value)
    }
    const url="http://127.0.0.1:5000/getdata"
    const [stu, setAttn]=useState(null)
    let content=null
    useEffect(()=>{
    axios.get(url)
        .then(res=>{
            setAttn(res.data)
        })},[url])
    if(stu){
        content=
        <div><h1>{stu.nm.name}</h1></div>
    }
    
return(
    <div>
    <div>Enter name of Student: </div>
    <input type="text"></input>
    <button onClick={setdt(true)}>GET ATTENDANCE</button>
   
<div>{content}</div>
</div>
)
}

export default teeUi;