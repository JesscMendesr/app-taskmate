from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
import bcrypt


# Configurações
SECRET_KEY = "sua_chave_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def criar_token(usuario_id: int):
    dados = {"sub": str(usuario_id)}
    expiracao = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    dados.update({"exp": expiracao})
    token = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return token

def get_usuario_atual(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario_id = int(payload.get("sub"))
        if usuario_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciais inválidas",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return usuario_id
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
def criptografar_senha(senha: str) -> str:
    # Gera um salt e faz o hash da senha
    salt = bcrypt.gensalt()
    senha_criptografada = bcrypt.hashpw(senha.encode('utf-8'), salt)
    return senha_criptografada.decode('utf-8')

def verificar_senha(senha: str, senha_criptografada: str) -> bool:
    # Verifica se a senha corresponde ao hash
    return bcrypt.checkpw(senha.encode('utf-8'), senha_criptografada.encode('utf-8'))