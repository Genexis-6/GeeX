import {  type UseFormSetError, } from "react-hook-form";
import { type RegFormInputs } from "./form_input_dec";
import { DefaultRequest } from "../../../utils/http/default_request";
import type { RegistrationResInterface } from "../models/response/auth/registration_res_interface";
import { RegistrationModel } from "../models/data/auth/registration_model";
import { BackendUrlPaths } from "../../../utils/config/backend_url_paths";
import type { BackendApiRes } from "../../../utils/config/backend_api_response";

type RegFuncParam = {
    data:RegFormInputs,
    setError: UseFormSetError<RegFormInputs>
}
export class HandleAuthFormSubmission {


    static async register({data, setError}:RegFuncParam){
        let regData: RegistrationModel = new RegistrationModel({firstname:data.firstname,lastname: data.lastname,phone: data.phone,email: data.email,password: data.password})
        const res = await DefaultRequest.post<RegistrationModel, BackendApiRes<RegistrationResInterface>>({url:BackendUrlPaths.registration, payload:regData})
        if(res.statusCode == 403){
            setError("email", {
                message:res.message
            })
        }
    }
}