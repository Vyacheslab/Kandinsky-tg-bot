import base64
import sqlite3

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from generator import Text2ImageAPI
from app.keyboards import start_keyboard
from datetime import datetime, timedelta


router3 = Router()


@router3.message(F.text == ('Генерация'))
async def command_test3(message: Message):
    await message.answer('Используйте команду /gen чтобы сгенерировать изображение.\n📸 Можете писать как на английском, так и на русском.\nПример: /gen пушистый кот или /gen black cat')

@router3.message(Command('start'))
async def command_test3(message: Message):
    await message.answer('Привет. Используйте команду /gen чтобы сгенерировать изображение.')


@router3.message(Command('gen'))
async def command_test(message: Message) -> None:

    text = message.text
    text2 = text.replace("/gen", "").strip()
    await message.answer(f'Генерируем {text2}, пожалуйста, подождите.')
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', 'Ваш 1 токен',
                        'ВАШ 2 токен')
    model_id = api.get_model()
    uuid = api.generate(text2, model_id)
    images = api.check_generation(uuid)
    result = images[0].strip("[]")
    imgdata = base64.b64decode(result)
    filename = 'test.png'
    with open(filename, 'wb') as f:
        f.write(imgdata)
    cat = FSInputFile("test.png")
    await message.answer_photo(photo=cat)
    connect.close()
