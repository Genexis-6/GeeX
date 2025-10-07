export class FormInputValidators {
  /**
   * Validate name (only letters and spaces allowed)
   */
  static validateName(userInput: string, fieldName: string): string | boolean {
    const trimmed = userInput.trim();

    if (trimmed === "") {
      return `${fieldName} is required`;
    }

    // Only letters and spaces allowed
    const nameRegex = /^[A-Za-z\s]+$/;
    if (!nameRegex.test(trimmed)) {
      return `${fieldName} must contain only letters`;
    }

    return true;
  }

  static validatePhone(userInput: string):string | boolean{
    const data:string = userInput.trim()
    if(data  === ""){
        return "Phone number must not be empty"
    }else if(data.length < 10){
        return "Phone number too short"
    }
    return true
  }
  /**
   * Validate email using regex
   */
  static validateEmail(userInput: string): string | boolean {
    const trimmed = userInput.trim();

    if (trimmed === "") {
      return "Email must not be empty";
    }

    // Basic email regex
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(trimmed)) {
      return "Invalid email format";
    }

    return true;
  }

  /**
   * Validate password (min 8 chars, at least 1 uppercase, 1 lowercase, 1 number, 1 symbol)
   */
  static validatePassword(userInput: string): string | boolean {
    if (userInput.length < 8) {
      return "Password must be at least 8 characters long";
    }
    if(userInput.length > 15){
      return "Password must be at most 14 charaters long"
    }

    const passwordRegex =
      /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&._-])[A-Za-z\d@$!%*?&._-]{8,}$/;

    if (!passwordRegex.test(userInput)) {
      return "Password must include uppercase, lowercase, number, and symbol";
    }

    return true;
  }
}
