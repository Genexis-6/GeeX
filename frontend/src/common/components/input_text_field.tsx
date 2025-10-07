import {type UseFormRegisterReturn,type FieldError } from "react-hook-form"

export type inputParam = {
    lable: string,
    placeholder: string,
    id: string,
    name: string
    type?: string
    className?: string
    error?:FieldError
    readOnly:boolean
    registerInput?:UseFormRegisterReturn

}

export default function InputTextField({ placeholder,
    readOnly=false,
    id, name,
    type = "text",
    className, registerInput,  error}: inputParam) {

    return <div className="my-1">
        {/* <label className="form-label ">{lable}</label> */}
        <input
           {...registerInput}
           readOnly={readOnly}
            type={type}
            className={`form-control ${className}`}
            name={name}
            id={id}
            placeholder={placeholder}
        />
        <span className="text-danger validator">{error?.message}</span>
    </div>
}