from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from ..core.config import settings
from ..core.security import create_access_token, verify_password
from ..models.user import User, UserCreate
from ..services import clearbit, emailhunter

router = APIRouter()

@router.post("/register", response_model=User)
async def register(user: UserCreate):
    if not settings.USERS_OPEN_REGISTRATION:
        email_domain = user.email.split("@")[-1]
        if not emailhunter.verify_domain(email_domain):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email domain is not valid"
            )
        if emailhunter.email_exists(user.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
    user_dict = user.dict()
    if settings.CLEARBIT_API_KEY:
        clearbit_data = clearbit.enrich_person(user.email, settings.CLEARBIT_API_KEY)
        user_dict.update(clearbit_data)
    user_dict['id'] = 1 # Replace with proper implementation
    return User(**user_dict)

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

def authenticate_user(email: str, password: str) -> Optional[User]:
    # Replace with proper implementation
    user = User(email=email)
    hashed_password = "fakehashedpassword"
    if verify_password(password, hashed_password):
        return user
    return None