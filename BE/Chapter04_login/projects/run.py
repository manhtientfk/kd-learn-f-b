from fastapi.security import OAuth2PasswordBearer
from .setting import app
from .Routers.Login import login


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
app.include_router(login.router)
