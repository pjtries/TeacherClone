from fastapi import APIRouter
from ..schemas.auth_schema import LoginRequest, LoginResponse, UserResponse
from ..services.auth_service import auth_service

router = APIRouter()

@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest):
    """
    Endpoint to simulate user login.
    Delegates logic to the AuthService and validates against LoginResponse schema.
    """
    return auth_service.login_user(request.email)

@router.get("/me", response_model=UserResponse)
def me():
    """
    Endpoint to simulate getting current user details.
    Delegates logic to the AuthService.
    """
    return auth_service.get_current_user()
