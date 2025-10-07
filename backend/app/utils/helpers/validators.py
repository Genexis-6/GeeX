import re

class Validators:
    @staticmethod
    def validate_phone(phone: str) -> bool:
        """
        Validate a phone number.
        - Only digits allowed
        - Length between 10 and 15 digits
        """
        pattern = r"^\d{10,15}$"
        return bool(re.match(pattern, phone))