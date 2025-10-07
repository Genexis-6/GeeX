import { type inputParam } from "./input_text_field";
import { Eye, EyeClosed } from 'lucide-react';
import { useState } from "react";

export default function CustomPasswordField({
    placeholder,
    id,
    name,
    type = "password",
    className,
    readOnly = false,
    registerInput,
    error
}: inputParam) {

    const [passwordVisible, setPasswordVisible] = useState(false);
    return (
        <div className="my-2">
            {/* <label htmlFor={id} className="form-label">{lable}</label> */}

            <div className="position-relative">
                <input
                    {...registerInput}
                    readOnly={readOnly}
                    type={passwordVisible ? "text" : type}
                    className={`form-control pe-5 ${className}`}
                    name={name}
                    id={id}
                    placeholder={placeholder}
                />
                <span className="visibility-icon position-absolute" onClick={() => setPasswordVisible(prop => !prop)}>
                    {
                        passwordVisible ? <Eye size={20} /> : <EyeClosed size={20} />
                    }
                </span>
            </div>
            <span className="text-danger validator">{error?.message}</span>
        </div>
    );
}
