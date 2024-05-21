from aiogram import Router, F
from aiogram.types import Message


my_router = Router(name=__name__)


@my_router.message()
async def message_handler(message: Message):
    await message.answer('Hello from my router!')