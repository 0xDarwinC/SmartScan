import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import upsLogo from "../../assets/ups-logo.png";
import { HeaderBar } from "../../navigation";
import React from "react";

export default function Dashboard() {

const navigate = useNavigate();

return (
    <div className="flex flex-col">
        <div>
            <HeaderBar
                headerIcon={upsLogo}
                headerTitle="Dashboard"
            />
        </div>
    </div>
);
}