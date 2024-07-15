import React from 'react'
import { BrowserRouter } from 'react-router-dom'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'

const e = document.getElementById("tabcontent");
const potentialTexts = e?.getElementsByClassName("dds__mb-4 content-heading_details");
let text = "";
if(potentialTexts){
  for (let i = 0; i<potentialTexts.length;i++){
    if (potentialTexts[i].tagName === "DIV"){
      for(const child of potentialTexts[i].children){
        if(child.tagName === "P"){
          text += child.textContent;
        }
      }
    }
  }
}

ReactDOM.createRoot(document.getElementById('root')!).render(
  <BrowserRouter><React.StrictMode>
  <App data={text} />
</React.StrictMode></BrowserRouter>
)
