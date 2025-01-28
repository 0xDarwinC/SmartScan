import React from 'react';  
import ReactDOM from "react-dom/client";  

import App from "./App.tsx";  
import "./index.css";

function main() {    
  ReactDOM.render(  
    <React.StrictMode>  
      <div className="font-sans">  
        <App/>  
      </div>  
    </React.StrictMode>,  
    document.getElementById('root')
  );  
}  
  
main();  