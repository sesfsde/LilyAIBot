import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

BOT_TOKEN = "8622623905:AAHkFpFQqVMoQsq-jdKtcXSgjpojpDDjiik"

# Основной URL Mini App (для моделей)
MINI_APP_URL = "https://lilian-ai-app.sesfsde.workers.dev"
# URL с параметром, чтобы сразу открыть тарифы для студий
STUDIO_URL = "https://lilian-ai-app.sesfsde.workers.dev?tab=shop&audience=studios"

DOWNLOAD_URL = "https://drive.google.com/drive/folders/1SWarkj4q4mf-2uIHum__FcVE8B2HYZnN?usp=drive_link"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def main_menu():
    buttons = [
        [InlineKeyboardButton(text="📥 Инструкция", callback_data="install")],
        [InlineKeyboardButton(text="❓ Частые вопросы", callback_data="faq")],
        [InlineKeyboardButton(text="💬 Поддержка", callback_data="support")],
        [InlineKeyboardButton(text="🔗 Скачать расширение", callback_data="download")],
        [InlineKeyboardButton(text="💎 Тарифы и оплата", web_app=WebAppInfo(url=MINI_APP_URL))],
        [InlineKeyboardButton(text="🏢 Владельцам студий", web_app=WebAppInfo(url=STUDIO_URL))]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

@dp.message(Command("start"))
async def start_command(message: types.Message):
    welcome_text = (
        "🌸 Привет! Я Lily AI – твой личный ИИ-ассистент для вебкам-моделей.\n\n"
        "Я помогу тебе:\n"
        "- Отвечать мемберам в чате 24/7\n"
        "- Копировать твой стиль (смайлики, обращения)\n"
        "- Анализировать мембера и подбирать тактику\n"
        "- Запоминать каждого мембера и твои заметки\n"
        "- Мягко подводить к привату или Lovense\n\n"
        "🎁 Сразу после привязки ника — <b>3 дня бесплатно</b> (10 генераций в день)!\n"
        "Затем можно выбрать тариф STANDARD ($149/мес) или PRO QUEEN ($349/мес).\n"
        "Для студий — специальные пакеты от $159/место.\n\n"
        "👇 Жми на кнопку, чтобы начать"
    )
    await message.answer(welcome_text, reply_markup=main_menu(), parse_mode="HTML")

@dp.callback_query()
async def handle_callback(callback: types.CallbackQuery):
    await callback.answer()
    if callback.data == "install":
        text = (
            "📥 <b>Инструкция по установке</b>\n\n"
            "1. Скачай архив по ссылке ниже.\n"
            f"📍 <a href='{DOWNLOAD_URL}'>Ссылка на архив</a>\n\n"
            "2. Распакуй архив в любую папку.\n\n"
            "3. Открой Chrome и перейди на страницу <code>chrome://extensions/</code>\n\n"
            "4. Включи «Режим разработчика».\n\n"
            "5. Нажми «Загрузить распакованное расширение» и выбери папку с распакованным архивом.\n\n"
            "6. После установки зайди на сайт Stripchat/Chaturbate (ВАЖНО: работает только на английской версси Chaturbate),  выполни вход с никнеймом, который ты указала в Telegram.\n\n"
            "7. Открой приватный чат и пользуйся!"
        )
        await callback.message.edit_text(text, reply_markup=main_menu(), parse_mode="HTML")
    elif callback.data == "faq":
        text = (
            "❓ <b>Часто задаваемые вопросы</b>\n\n"
            "1. Расширение не видит сообщения в чате\n"
            "→ Убедись, что ты открыла приватный чат (PM). Обнови страницу и перезагрузи расширение.\n\n"
            "2. ИИ не использует мои смайлики\n"
            "→ Заполни стиль в Telegram Mini App (Профиль → Настройка стиля Lily) и сохрани.\n\n"
            "3. Как ИИ узнаёт моё имя/возраст?\n"
            "→ Введи их в Telegram Mini App (Профиль → Личные данные).\n\n"
            "4. Как обновить расширение?\n"
            "→ Скачай новый архив, замени папку и перезагрузи в chrome://extensions\n\n"
            "5. Где смотреть срок подписки?\n"
            "→ Во вкладке «Профиль» Telegram Mini App.\n\n"
            "6. Почему долгий ответ?\n"
            "→ ИИ генерирует ответы 3-7 секунд. Если дольше — проверь интернет.\n\n"
            "7. Есть ли пробный период?\n"
            "→ Да! После привязки ника даётся <b>3 дня бесплатно</b> (10 генераций в день). Тариф START больше не используется."
        )
        await callback.message.edit_text(text, reply_markup=main_menu(), parse_mode="HTML")
    elif callback.data == "support":
        text = (
            "💬 <b>Служба поддержки Lily AI</b>\n\n"
            "Если у тебя возникли проблемы с установкой, оплатой или работой расширения – напиши нам.\n\n"
            "📱 Telegram: @Lily_AI_support"
        )
        await callback.message.edit_text(text, reply_markup=main_menu(), parse_mode="HTML")
    elif callback.data == "download":
        text = f"🔗 <b>Скачать расширение Lily AI</b>\n\n<a href='{DOWNLOAD_URL}'>Открыть папку с архивом</a>"
        await callback.message.edit_text(text, reply_markup=main_menu(), parse_mode="HTML")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
