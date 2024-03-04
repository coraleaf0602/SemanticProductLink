import "./App.css";
//import Sidebar from "./Components/SideBar";
//import Product from "./Components/ProductBar";
import { useState, } from "react";
import "./styles.css"
import SideBar3 from "./SideBar3";

function App() {
  const [inputText, setInputText] = useState("");
  const [responseData,setResponseData] = useState([]);

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputText(event.target.value);
  };

  function handleTextSubmit (text:string) {
    fetch("http://127.0.0.1:5000/start-task",{
      method:"POST",
      headers:{
        "Content-Type":"application/json"
      },
      body:JSON.stringify({"text":text})
    })
    .then((response) => {return response.json()}).then((data) => {
      return new Promise((resolve) => {
        const callback = () => { 
            fetch(`http://127.0.0.1:5000/get-task?job=${data.job}`)
            .then((res) => {
                if (res.status === 200){
                    resolve(res)
                }
                else{setTimeout(callback,1000)}  
            })
        }
        callback()
      })
    })
    .then((res:any) => {return res.json()})
    .then((data) => {console.log(data);setResponseData(data.category_links)})
    .catch(err => console.error(err));
  }
  return (
    <>
      <div className="mb-3">
      <label htmlFor="exampleFormControlInput1" className="form-label">
        Enter Text
      </label>
      <input
        type="Text"
        className="form-control"
        id="exampleFormControlInput1"
        placeholder="E.G. Docking Station"
        value={inputText}
        onChange={handleChange}
      />
      <button className="btn btn-primary" onClick={(event) => {event.preventDefault();handleTextSubmit(inputText)}}>
        Submit
      </button>
    </div>
      <div>
        {/* Display the submitted text }*/}
        {inputText && <div>Submitted Text: {inputText}</div>}
      </div>
      <div>
        <SideBar3 responseData={responseData}></SideBar3>
      </div>
    </>
  );
}

export default App;
