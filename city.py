from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
City = InlineKeyboardMarkup(
    inline_keyboard= [
    [
    InlineKeyboardButton(text="Toshkent shahar",callback_data='Tashkent'),
    InlineKeyboardButton(text="Farg'ana",callback_data='Fergana'),
    InlineKeyboardButton(text="Andijon",callback_data='Andijan'),
    ],
    [
    InlineKeyboardButton(text="Namangan",callback_data='Namangan'),
    InlineKeyboardButton(text="Jizzax",callback_data='Jizzakh'),
    InlineKeyboardButton(text="Sirdaryo",callback_data='Sirdaryo'),
    ],
    [
    InlineKeyboardButton(text="Qashqadaryo",callback_data='Qashqadaryo'),
    InlineKeyboardButton(text="Surxandaryo",callback_data='Termez'),
    InlineKeyboardButton(text="Navoiy",callback_data='Navoi'),
    ],
    [
    InlineKeyboardButton(text="Buxoro",callback_data='Bukhara'),
    InlineKeyboardButton(text="Xorazim",callback_data='Urganch'),
    InlineKeyboardButton(text="Toshkent viloyati",callback_data='Tashkent'),
    ],
    [
    InlineKeyboardButton(text="Qoraqalpog'iston",callback_data='Karakalpakstan'),
    ],
    ]
)