import React, { useState } from "react";

interface Props {
  displayText: (text: string) => void;
}

const TextBox: React.FC<Props> = ({ displayText }) => {
  const [inputText, setInputText] = useState("");

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputText(event.target.value);
  };

  const handleSubmit = () => {
    displayText(inputText);
    setInputText("");
  };

  return (
    <div className="mb-3">
      <label htmlFor="exampleFormControlInput1" className="form-label">
        Enter Text
      </label>
      <input
        type="text"
        className="form-control"
        id="exampleFormControlInput1"
        placeholder="E.G. Docking Station"
        value={inputText}
        onChange={handleChange}
      />
      <button className="btn btn-primary" onClick={handleSubmit}>
        Submit
      </button>
    </div>
  );
};

export default TextBox;

/*interface props {
  children: string;
  onClick: () => void;
   displayText:  () => void;
}
const TextBox = ({ children, onClick, displayText }: props) => {
  return (
    <div className="mb-3">
      <label htmlFor={children} className="form-label">
        Enter Text
      </label>
      <input
        type="email"
        className="form-control"
        id="exampleFormControlInput1"
        placeholder="E.G. Docking Station"
      ></input>
      <button className={"btn btn-primary"} onClick={displayText}>
        Submit
      </button>
    </div>
  );
};

export default TextBox; */
