from fastapi.security import OAuth2PasswordBearer
from .setting import app
from .Routers.Login import login
from .Routers.Candicate import candicate


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
app.include_router(login.router)
app.include_router(candicate.router)
