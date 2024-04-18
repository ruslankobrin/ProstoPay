import asyncio
import unittest
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_scoped_session,
)
from sqlalchemy.orm import sessionmaker

from task_2 import UserManager, User, UserDTO


class TestUserManager(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=True)
        async_session = async_scoped_session(
            sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False),
            scopefunc=asyncio.current_task,
        )
        async with engine.begin() as conn:
            await conn.run_sync(User.metadata.create_all)
        self.repo = UserManager(async_session)

    async def test_add_get_user(self):
        user = UserDTO(id=1, username="test_user", email="test@example.com")

        # Add user
        await self.repo.add(user)

        # Get user and assert
        retrieved_user = await self.repo.get(user.id)
        self.assertEqual(retrieved_user, user)

    async def test_get_none_existent_user(self):
        with self.assertRaises(ValueError):
            await self.repo.get(100)


if __name__ == "__main__":
    unittest.main()
