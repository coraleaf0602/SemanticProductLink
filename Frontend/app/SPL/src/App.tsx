import "./App.css";
//import Sidebar from "./Components/SideBar";
//import Product from "./Components/ProductBar";
import "./styles.css"
import CircularProgress from "@mui/material/CircularProgress";
import Box from "@mui/material/Box"
import SideBar3 from "./SideBar3";
import { useEffect, useState } from "react";
const url = "https://demo.greenpond-fd41f303.westeurope.azurecontainerapps.io";

function App(data:any) {
  const [responseData,setResponseData] = useState([]);
  const [finished,setFinished] = useState(false);

  useEffect(() =>{
    if(data !== "") {
      console.log(data.data);
      fetch(`${url}/start-task`,{
      method:"POST",
      headers:{
        "Content-Type":"application/json"
      },
      body:JSON.stringify({"text":data.data})
    })
    .then((response) => {return response.json()}).then((data) => {
      return new Promise((resolve,reject) => {
        let attempts = 0;
        const callback = () => { 
            fetch(`${url}/get-task?job=${data.job}`)
            .then((res) => {
                if (res.status === 200){
                    resolve(res)
                } else if(attempts === 5){
                  reject("Too many attempts");
                }
                else{attempts++;setTimeout(callback,1000)}  
            })
        }
        callback()
      })
    })
    .then((res:any) => {return res.json()})
    .then((data) => {setResponseData(data.category_links);setFinished(true)})
    .catch(err => console.error(err));
    }
  },[data])

  return(!finished?<Box className = "nav-menu-items"><CircularProgress /></Box>:<SideBar3 dataList={responseData}/>)
}

export default App;
