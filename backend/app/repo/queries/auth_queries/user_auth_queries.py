from .. import *
from app.security.hash_password.password import generate_password, verify_hash_password
import uuid
from app.utils.helpers.validators import Validators
from app.utils.enums.jwt_roles import JWTroles




class UsersAuthQueries:
    def __init__(self, db: AsyncSession):
        self.session = db
    
    async def check_user_exist(self, email:str):
        res = await self.session.execute(select(Users).where(Users.email == email))
        output = res.scalar_one_or_none()
        return output
    
    async def create_user_account(self, user: CreateUserAccountSchemas):
        try:
            if Validators.validate_phone(user.phone):
                output = await self.check_user_exist(user.email)
                if output is None:
                    self.session.add(
                        Users(
                            id = uuid.uuid4(),
                            name = user.name,
                            email = str(user.email),
                            phone = user.phone,
                            role = JWTroles.USER,
                            password = generate_password(user.password)
                        )
                    )
                    await self.session.commit()
                    return AuthEnums.CREATED
                return AuthEnums.EXIST
            
            return AuthEnums.INVALID_PHONE_NUMBER
            
        except Exception as e:
            print(f"error due to: {e}")
            return AuthEnums.FAILED
        
    async def login_user(self, user_data):
        res = await self.check_user_exist(user_data.username)
        try:
            if res:
                if verify_hash_password(user_data.password, hash_pass=res.password):
                    return res
                return AuthEnums.ACCECC_NOT_GRANTED
            return AuthEnums.NONE_FOUND
        except Exception as e:
            print(f"error logging in due to: {e}")
            return AuthEnums.FAILED
        
        
            
        