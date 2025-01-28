import React from "react";
import HeaderBarTitle from "./HeaderBarTitle";

interface HeaderBarProps {
    headerIcon: any;
    headerTitle: string;
    headerMenuTitle?: string;
}

export default function HeaderBar ({
    headerIcon,
    headerTitle,
}: HeaderBarProps) {
    return(
        <div className="fixed left-0 top-0 z-50 flex w-full items-center justify0between bg-[#121212] px-4 py-2">
            <HeaderBarTitle title={headerTitle} icon={headerIcon}/>
        </div>
    );
}