from fastapi import APIRouter
from core import system, cpu

router = APIRouter()

@router.get('/system')
async def get_system():
    return system.get_system_info()

@router.get('/cpu')
async def get_cpu():
    return cpu.get_cpu_info()