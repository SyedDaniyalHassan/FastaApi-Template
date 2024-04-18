from fastapi.routing import APIRouter

from basic_app.web.api import dummy, echo, monitoring, users

api_router = APIRouter()
api_router.include_router(monitoring.router, tags=["healthCheck"])
api_router.include_router(users.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(dummy.router, prefix="/dummy", tags=["dummy"])
