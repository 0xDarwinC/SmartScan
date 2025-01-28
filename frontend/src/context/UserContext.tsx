import React, { createContext, useState } from "react";  

import { RoleType } from "../components/overgoods/types"
  
export interface UserInfo {  
  name: string;
  role: RoleType["role_name"];  
  access: string;  
}  
  
interface UserContextType {  
  user: UserInfo | undefined;  
  setUser: (user: UserInfo | undefined) => void;  
}  
  
export interface UserContextType {
  user: UserInfo | undefined;
  setUser: (user: UserInfo | undefined) => void;
}

export const UserContext = createContext <UserContextType| undefined>(
  undefined
);

export default function UserProvider({
  children,
}: {
  children: React.ReactNode;
}) {
  const [user, setUser] = useState<UserInfo | undefined> (undefined);

  return (
    <UserContext.Provider value={{ user, setUser }}>
      {children}
    </UserContext.Provider>
  );
}

