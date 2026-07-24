from fastapi import APIRouter
from core import system

router = APIRouter()

@router.get('/system')
async def get_system():
    return system.get_system_info()