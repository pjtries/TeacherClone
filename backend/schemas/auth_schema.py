from pydantic import BaseModel

class LoginRequest(BaseModel):
    """Schema for login request."""
    email: str

class UserResponse(BaseModel):
    """Schema for basic user details."""
    id: str
    name: str
    email: str

class LoginResponse(BaseModel):
    """Schema for login response including user and token."""
    user: UserResponse
    token: str
