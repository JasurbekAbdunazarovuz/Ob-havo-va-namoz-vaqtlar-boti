from aiogram.types import Message, User, KeyboardButton, InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery
from aiogram import Router, Dispatcher, Bot
from aiogram.filters.command import Command
from asyncio import run
from abc import ABC, abstractmethod
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from weather_api import get_date
from namoz_vaqtlari import mintaqalar,oylar,vaqti
from city import City
from ortga import ortga_tugma
from namoz import namoz_t
from config import BOT_TOKEN

greet = Router()

@greet.message(Command(commands=["start"]))
async def greet_message(msg: Message, bot: Bot):
    await msg.answer("Assalomu alaykum bo'timizga hush kelibsiz🤗\nBu 12 viloyat ob-havo ma'lumoti boti⛅️\nMa'lumot olish uchun /weather tugmasini bosing🥲")


@greet.message(Command(commands=["weather"]))
async def greet_messag(msg: Message, bot: Bot):
    await msg.answer("Assalomu alaykum 12 viloyat ob-havo ma'lumoti bo'limiga hush kelibsiz, siz qaysi viloyatning ob-havosi haqida bilmoqchisiz?⛅️\nOb-havo ma'lumotini bilish uchun tugmalardan birini tanlang☺️",reply_markup=City)



@greet.message(Command(commands=["namoz_vaqtlari"]))
async def greet_messag(msg: Message, bot: Bot):
    await msg.answer("Namoz vaqtlarini bilish?",reply_markup=namoz_t)


@greet.callback_query()
async def namoz_time(call:CallbackQuery):
    if call.data == "back":
        await call.message.edit_text("Namoz vaqtlarini bilish?",reply_markup=namoz_t)
    elif call.data.isdigit():
        m = int(call.data)
        content = vaqti(m)
        print(content)
        text = f"""{content[2]} kungi namoz vaqtlari:
    Bomdod: {content[3]}
    Quyosh: {content[4]}
    Peshin: {content[5]}
    Asr: {content[6]}
    Shom: {content[7]}
    Xufton: {content[8]}
        """
        await call.message.edit_text(text,reply_markup=ortga_tugma)
    else:
        city = call.data
        weather = round(get_date(city),2)
        await call.answer(f"{weather}°C")





async def start():
    dp = Dispatcher()
    bot = BOT_TOKEN
    dp.include_router(greet)
    try:
        await dp.start_polling(bot)
    except:
        await bot.session.close()

if __name__ == "__main__":
    run(start())