__all__ = ()


from fastapi import APIRouter
from .user_router import router as user_router
from .auth import router as auth_router
from .type_router import router as type_router
from .brand_router import router as brand_router
from .device_router import router as device_router

router = APIRouter(prefix="/api")


router.include_router(auth_router)
router.include_router(user_router)
router.include_router(type_router)
router.include_router(brand_router)
router.include_router(device_router)
