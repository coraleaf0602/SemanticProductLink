import TextBox from "./TextBox";
import "./App.css";
//import Sidebar from "./Components/SideBar";
//import Product from "./Components/ProductBar";
import { SetStateAction, useState } from "react";
import SideBar3 from "./SideBar3";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  const [submittedText, setSubmittedText] = useState("");

  const handleDisplayText = (text: SetStateAction<string>) => {
    setSubmittedText(text);
  };

  return (
    <>
      <div>
        <TextBox displayText={handleDisplayText} />
        {/* Display the submitted text }*/}
        {submittedText && <div>Submitted Text: {submittedText}</div>}
        {/*<Product
          x={0}
          y={20}
          width={150}
          height={625}
          imageSrc={"./xps2Standard.jpg"}
          onMouseOver={console.log}
          onMouseOut={console.log}
          hh
        />*/}
      </div>
      <Router>
        <SideBar3 />
        <Routes>
          <Route path="/" />
        </Routes>
      </Router>
    </>
  );
}

export default App;
