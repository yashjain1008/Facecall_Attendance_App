import { render } from "@testing-library/react";
import axios from "axios";
import React,{useState,useEffect} from "react";


// export default see;
function SeeUi() {
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
        <div><h1>{stu.HARSH.name}</h1></div>
    }
    
return(
    
    <div>{content}</div>
)
}

export default SeeUi;