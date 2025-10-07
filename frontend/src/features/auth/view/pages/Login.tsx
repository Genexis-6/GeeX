import "../styles/login.css"
import GImage1 from "../../../../assets/images/jpgs/Gmage2.jpg"
import { useForm } from "react-hook-form"
import InputTextField from "../../../../common/components/input_text_field"
import { FormInputValidators } from "../../../../utils/validators/form_input_validators"
import type { LoginFormInput } from "../../controllers/form_input_dec"
import CustomPasswordField from "../../../../common/components/custom_password_field"
import { NavLink } from "react-router-dom"
import { AllAppUrlPath } from "../../../../utils/routes/urls/all_app_urls"
import FormFooterSection from "../components/form_footer_section"
import DefaultButton from "../../../../common/components/default_button"



export default function Login() {
    const { register, setError, handleSubmit, formState: { errors, isSubmitting } } = useForm<LoginFormInput>()
    return <>
        <div className="container-fluid login-page  px-2 px-md-0">
            <div className="row h-100">
                <div className="col-lg-5 d-flex flex-column justify-content-center align-items-center">
                    <div className="login-form-container">
                        <div className="col-12 mb-2 heading">
                            <h2>Welcome back!</h2>
                            <p>some greeting text</p>
                        </div>
                        <form>
                            <div className="row">
                                <div className="col-12">
                                    <InputTextField
                                        readOnly={true}
                                        registerInput={register("email", {
                                            validate: (e) => FormInputValidators.validateEmail(e)
                                        })}
                                        error={errors.email}
                                        name="email" lable="Email Address"
                                        id="email" placeholder="john@example.com"
                                    />
                                </div>
                            </div>
                            <div className="row">
                                <div className="col-12">
                                    <CustomPasswordField
                                        readOnly={isSubmitting}
                                        registerInput={register("password", {
                                            validate: (e) => FormInputValidators.validatePassword(e)
                                        })}
                                        error={errors.password}
                                        name="password" lable="Password"
                                        id="password" placeholder="password"
                                    />
                                </div>
                            </div>
                            <div className="row">
                                <div className="col-12 d-flex justify-content-end forget-password">
                                    <NavLink to={AllAppUrlPath.forgetPasswordPath}>
                                        <p>forget password?</p>
                                    </NavLink>
                                </div>
                            </div>
                            <div className="row">
                                <div className="col-12">
                                    <DefaultButton title={"submit"} operation={() => { }} />
                                </div>
                            </div>
                            <div className="row">
                                <div className="col-12">
                                    <FormFooterSection text={"signin"} />
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
                <div className="col-lg-7  h-100 d-none d-lg-block g-image">
                    <img src={GImage1} alt="BG-IMAGE" />
                </div>
            </div>
        </div>
    </>
}