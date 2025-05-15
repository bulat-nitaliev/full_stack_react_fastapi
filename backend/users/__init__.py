from users.userprofile.handlers import router as user_router
from users.auth.handlers import router as auth_router

__all__ = (
    "user_router",
    "auth_router"
)