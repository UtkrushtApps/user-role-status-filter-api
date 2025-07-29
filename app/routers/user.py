from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.models.user import UserResponse
from typing import List, Optional
from app.services.user_service import list_users_service

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[UserResponse])
async def list_users(role: Optional[str] = None, status: Optional[str] = None, db: AsyncSession = Depends(get_db)):
    pass
