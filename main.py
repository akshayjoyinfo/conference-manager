
import logging
from fastapi import FastAPI
from starlette.requests import Request
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import JSONResponse

from controllers.health.status import health_router
from controllers.v1.conference import conference_router

from config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

logging.config.fileConfig('logger.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)

@app.exception_handler(Exception)
async def exception_callback(request: Request, exc: Exception):
    logging.info('API Unhandled Error', exc_info=True)
    return JSONResponse({"detail": "Unknown Error"}, status_code=500)

app.include_router(health_router, tags=["HealthCheck"])
app.include_router(conference_router, tags=["Conference"])
