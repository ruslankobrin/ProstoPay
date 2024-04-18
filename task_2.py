from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)


class UserDTO(BaseModel):
    id: int
    username: str
    email: str


class UserManager:
    def __init__(self, async_session: AsyncSession):
        self.async_session = async_session

    async def get(self, user_id: int) -> UserDTO:
        async with self.async_session() as session:
            result = await session.execute(select(User).filter(User.id == user_id))
            user = result.scalars().first()
            if not user:
                raise ValueError(f"User with id {user_id} not found")
            return UserDTO(id=user.id, username=user.username, email=user.email)

    async def add(self, user: UserDTO) -> None:
        async with self.async_session() as session:
            new_user = User(id=user.id, username=user.username, email=user.email)
            session.add(new_user)
            await session.commit()
