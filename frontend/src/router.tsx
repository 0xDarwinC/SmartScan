import React from 'react';  
import { BrowserRouter, Route, Routes } from "react-router-dom";  
import { useUser } from "./context";  
import Dashboard from "./components/overgoods/pages/Dashboard";  
  
export default function Router() {    
    const { user } = useUser();    
  
    return user ? (    
        <BrowserRouter>    
            <Routes>    
                <Route path="/" element={<Dashboard />} />    
            </Routes>    
        </BrowserRouter>    
    ) : null;    
};  