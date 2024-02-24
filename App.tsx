import TextBox from "./Components/TextBox";
import { SetStateAction, useState } from "react";

function App() {
  const [submittedText, setSubmittedText] = useState("");

  const handleDisplayText = (text: SetStateAction<string>) => {
    setSubmittedText(text);
  };

  return (
    <div>
      <TextBox displayText={handleDisplayText} />
      {/* Display the submitted text */}
      {submittedText && <div>Submitted Text: {submittedText}</div>}
    </div>
  );
}

export default App;
