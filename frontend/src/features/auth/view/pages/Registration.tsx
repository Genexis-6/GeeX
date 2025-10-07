import "../styles/registration.css"
import InputTextField from "../../../../common/components/input_text_field"
import FormFooterSection from "../components/form_footer_section"
import CustomPasswordField from "../../../../common/components/custom_password_field"
import DefaultButton from "../../../../common/components/default_button"
import { useForm, type SubmitHandler } from "react-hook-form"
import { FormInputValidators } from "../../../../utils/validators/form_input_validators"
import { HandleAuthFormSubmission } from "../../controllers/handle_auth_form_submission"
import { type RegFormInputs } from "../../controllers/form_input_dec"
import OnBoardingHeaderSection from "../components/onboarding_header_section"
// import GImage from "../../../../assets/images/jpgs/Gmage1.jpg"
import LoadingSpinner from "../../../../common/components/loading_spinner"
import GImage1 from "../../../../assets/images/jpgs/Gmage2.jpg"
import { NavLink } from "react-router-dom"
import { AllAppUrlPath } from "../../../../utils/routes/urls/all_app_urls"




export default function Registration() {
    const { register, setError, handleSubmit, formState: { errors, isSubmitting } } = useForm<RegFormInputs>()

    const onSubmit: SubmitHandler<RegFormInputs> = async (data) => {
        await HandleAuthFormSubmission.register({ data: data, setError: setError })
    }
    return <>
        <div className="container-fluid px-2 px-md-0 registration-page">
            <div className="row h-100">
                <div className="col-lg-5 d-flex flex-column justify-content-center align-items-center">
                    <div className="row">
                        <div className="col-12 mt-2 ">
                            {isSubmitting && <LoadingSpinner />}
                        </div>
                        <div className="col-12 d-flex justify-content-center">
                            <form className="reg-form-section" onSubmit={handleSubmit(onSubmit)}>
                                <div className="row">
                                    <div className="col-12 mb-2 heading">
                                        <h2>Create an account</h2>
                                        <p>Aleady have an account?
                                            <NavLink to={AllAppUrlPath.loginPath}>
                                                <span className="mx-1">Login</span>
                                            </NavLink>
                                        </p>
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-6">
                                        <InputTextField
                                            readOnly={isSubmitting}
                                            registerInput={register("firstname", {
                                                validate: (e) => FormInputValidators.validateName(e, "first name")
                                            })}
                                            error={errors.firstname}
                                            name="firstname" lable="First Name"
                                            id="firstname" placeholder="first name"
                                        />
                                    </div>
                                    <div className="col-6">
                                        <InputTextField
                                            readOnly={isSubmitting}
                                            registerInput={register("lastname", {
                                                validate: (e) => FormInputValidators.validateName(e, "last name")
                                            })}
                                            error={errors.lastname}
                                            name="lastname" lable="Last Name"
                                            id="lastname" placeholder="last name"
                                        />
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-12">
                                        <InputTextField
                                            readOnly={isSubmitting}
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
                                        <InputTextField
                                            readOnly={isSubmitting}
                                            registerInput={register("phone", {
                                                validate: (e) => FormInputValidators.validatePhone(e)
                                            })}
                                            error={errors.phone}
                                            name="phone" lable="Phone Number"
                                            id="phone" placeholder="080******10"
                                            type="number" className="no-spinner"
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
                                    <div className="col-12 d-flex justify-content-center mb-1">
                                        <DefaultButton
                                            disabled={isSubmitting}
                                            title={
                                                isSubmitting ? "submitting..." : "submit"
                                            } operation={() => { }} />
                                    </div>
                                </div>

                                <FormFooterSection text={"siginup"} />
                            </form>
                        </div>
                    </div>
                </div>
                <div className="col-lg-7   d-none d-lg-block g-image">
                    <img src={GImage1} alt="BG-IMAGE" />
                </div>
            </div>
        </div>
    </>
}