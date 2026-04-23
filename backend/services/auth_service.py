class AuthService:
    """ Service to handle mock authentication logic. """
    
    @staticmethod
    def login_user(email: str):
        """
        Simulates logging in a user.
        Logic: 
        - If email contains 'teacher', returns a mock teacher user.
        - Otherwise returns a mock student user.
        """
        email_lower = email.lower()
        
        if "teacher" in email_lower:
            user = {
                "id": "t1",
                "name": "Dr. Anderson",
                "email": email
            }
        else:
            user = {
                "id": "s1",
                "name": "Alex Student",
                "email": email
            }
            
        return {
            "user": user,
            "token": "mock-firebase-token-123456"
        }

    @staticmethod
    def get_current_user():
        """
        Returns the mock details of the currently authenticated user.
        """
        return {
            "id": "t1",
            "name": "Dr. Anderson",
            "email": "anderson@example.com"
        }

auth_service = AuthService()
