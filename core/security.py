from cryptography.fernet import Fernet
import jwt
from datetime import datetime, timedelta

class SecurityManager:
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
        self.fernet = Fernet(secret_key)
    
    def encrypt_credentials(self, credentials: Dict[str, Any]) -> str:
        return self.fernet.encrypt(json.dumps(credentials).encode())
    
    def decrypt_credentials(self, encrypted_data: str) -> Dict[str, Any]:
        return json.loads(self.fernet.decrypt(encrypted_data).decode())
    
    def generate_token(self, user_id: str) -> str:
        return jwt.encode(
            {
                'user_id': user_id,
                'exp': datetime.utcnow() + timedelta(hours=24)
            },
            self.secret_key,
            algorithm='HS256'
        ) 