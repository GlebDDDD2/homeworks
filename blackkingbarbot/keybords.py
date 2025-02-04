from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton
)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

class Pagination(CallbackData, prefix="pag"):
    action: str
    page: int

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/contacts - Контакты'),],
    [KeyboardButton(text='/register - регистрация')],
    [KeyboardButton(text='/afir - эфир ')],
    [KeyboardButton(text='/pagin - пагинацию')],
    [KeyboardButton(text='/profile - профиль')],
    [KeyboardButton(text='/info - О нас')]
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню...')

get_number = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отправить номер', request_contact=True)]
], resize_keyboard=True)

def paginator(page: int=1):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="⬅", callback_data=Pagination(action="prev", page=page).pack()),
        InlineKeyboardButton(text="➡", callback_data=Pagination(action="next", page=page).pack()),
        width=2
    )
    return builder.as_markup()