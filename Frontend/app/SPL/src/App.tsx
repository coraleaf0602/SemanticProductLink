import "./App.css";
//import Sidebar from "./Components/SideBar";
//import Product from "./Components/ProductBar";
import "./styles.css"
import CircularProgress from "@mui/material/CircularProgress";
import Box from "@mui/material/Box"
import SideBar3 from "./SideBar3";
import { useEffect, useState } from "react";

const link = "http://127.0.0.1:5000";

function App(input_data:any) {
  const [responseData,setResponseData] = useState([]);
  const [finished,setFinished] = useState(false);

  useEffect(() =>{
    if(input_data !== "") {
      fetch(`${link}/check`,{method:"GET",headers:{"text":input_data.data}})
      .then(async(res) => {
        let result = res 
        if(res.status !== 200){
          result = await fetch(`${link}/start-task`,{
          method:"POST",
          headers:{
            "Content-Type":"application/json"
          },
          body:JSON.stringify({"text":input_data.data})
          }).then((response) => {return response.json()}).then((data) => {
          let calls = 0;
          return new Promise((resolve,reject) => {
            const callback = () => { 
                fetch(`${link}/get-task?job=${data.job}`,{method:"GET",headers:{"text":input_data.data}})
                .then((res) => {
                    if (res.status === 200){
                        resolve(res)
                    } else if (calls === 4){
                      reject("Too many calls");
                    }
                    else{calls++;setTimeout(callback,1000)}  
                })
            }
            callback()
          })
        })
      } return result;
      }).then((res:any) => {return res.json()}).then((data) => {setResponseData(data.category_links);setFinished(true)}).catch(err => console.error(err));
    }
  },[input_data.data])

  return(!finished?<Box className = "nav-menu-items"><CircularProgress /></Box>:<SideBar3 dataList={responseData}/>)
}

export default App;
