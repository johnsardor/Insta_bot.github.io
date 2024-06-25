from aiogram.types import InlineKeyboardMarkup, KeyboardButton, WebhookInfo, ReplyKeyboardMarkup

web_app=WebhookInfo(url='https://www.instagram.com/')

app_kb=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Insta', web_app=web_app)]
], resize_keyboard=True)




