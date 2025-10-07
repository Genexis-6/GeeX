import type { RegFormInputs } from "../../../controllers/form_input_dec";


export class RegistrationModel{
    public name:string;
    public phone:string;
    public email:string;
    public password:string;

    constructor({firstname, lastname, phone, email, password}: RegFormInputs){
        this.name = `${firstname} ${lastname}`;
        this.phone = phone
        this.email = email,
        this.password = password
    }
    
}