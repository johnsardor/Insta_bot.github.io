from aiogram.types import InlineKeyboardMarkup, KeyboardButton, WebAppInfo, ReplyKeyboardMarkup

web_app=WebAppInfo(url='https://www.instagram.com/')

app_kb=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Instagram', web_app=web_app)]
], resize_keyboard=True)




