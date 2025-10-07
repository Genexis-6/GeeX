import googleIcon from "../../../../assets/images/svgs/googleIcon.svg"


export default function FormFooterSection({text}:{text:string}) {
    return (
        <div className="row mt-3 mb-1 ">
            <div className="col-12 d-flex justify-content-center ">
                <div className="w-100 d-flex align-items-center">
                    <hr className="flex-grow-1" />
                    <span className="mx-2">or {text} with</span>
                    <hr className="flex-grow-1" />
                </div>
            </div>

            <div className="col-12 d-flex justify-content-center mt-3">
                <div className="googleIcon" onClick={()=>console.log("wroking")}>
                    <img src={googleIcon} alt="google icon" /> <span>google</span>
                </div>
            </div>
        </div>
    );
}