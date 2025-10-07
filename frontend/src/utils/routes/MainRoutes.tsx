import { BrowserRouter, Route, Routes } from "react-router-dom";
import Registration from "../../features/auth/view/pages/Registration";
import Login from "../../features/auth/view/pages/Login";
import { AllAppUrlPath } from "./urls/all_app_urls";

export default function MainRoute() {
    return <BrowserRouter>
        <Routes >
            <Route path="/" element ={<Registration/>}/>
            <Route path={AllAppUrlPath.loginPath} element = {<Login/>}/>
        </Routes>
    </BrowserRouter>
}