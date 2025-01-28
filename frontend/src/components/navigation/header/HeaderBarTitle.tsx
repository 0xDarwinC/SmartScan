import React from "react";
import { Link } from "react-router-dom";  
  
interface HeaderBarTitleProps {  
    title: string;  
    icon: any;  
}  
  
export default function HeaderBarTitle({ title, icon }: HeaderBarTitleProps) {  
    return (  
        <div>  
            <div className="flex items-center">  
                <Link to="/" className="flex items-center">  
                    <img   
                        src={icon}  
                        alt="UPS Shield"  
                        className="items-left flex h-[2.38025rem] w-8"  
                    />  
                </Link>  
            </div>  
            <div className="ml-4 text-right text-xl font-normal leading-8 text-[#f4f4f4f]">  
                {title}  
            </div>  
        </div>  
    );  
}  
