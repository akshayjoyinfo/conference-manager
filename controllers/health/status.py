from fastapi import APIRouter

health_router = APIRouter()


@health_router.get('/health')
def index():
    return {'status': 'Healthy'}
