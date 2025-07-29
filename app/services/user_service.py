from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, List
from app.models.user import UserResponse

async def list_users_service(role: Optional[str], status: Optional[str], db: AsyncSession) -> List[UserResponse]:
    pass
