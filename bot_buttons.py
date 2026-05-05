import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

BOT_TOKEN = "8622623905:AAHkFpFQqVMoQsq-jdKtcXSgjpojpDDjiik"

MINI_APP_URL = "https://lilian-ai-app.sesfsde.workers.dev"
DOWNLOAD_URL = "https://drive.google.com/drive/folders/1SWarkj4q4mf-2uIHum__FcVE8B2HYZnN?usp=sharing"
NEWS_CHANNEL_URL = "https://t.me/LilyAI_News"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def main_menu():
    buttons = [
        [InlineKeyboardButton(text="📥 Инструкция", callback_data="install")],
        [InlineKeyboardButton(text="❓ Частые вопросы", callback_data="faq")],
        [InlineKeyboardButton(text="💬 Поддержка", callback_data="support")],
        [InlineKeyboardButton(text="🔗 Скачать расширение", callback_data="download")],
        [InlineKeyboardButton(text="📢 Новости", url=NEWS_CHANNEL_URL)],
        [InlineKeyboardButton(text="💎 Тарифы и оплата", web_app=WebAppInfo(url=MINI_APP_URL))]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

@dp.message(Command("start"))
async def start_command(message: types.Message):
    welcome_text = (
        "🌸 Привет! Я Lily AI – твой личный ассистент для вебкам-моделей.\n\n"
        "Я помогу тебе:\n"
        "- Отвечать мемберам в чате 24/7\n"
        "- Копировать твой стиль (смайлики, обращения)\n"
        "- Анализировать тип мембера и подбирать тактику\n"
        "- Запоминать каждого мембера и твои заметки о нём\n"
        "- Мягко подводить к привату или Lovense\n\n"
        "👇 Нажми на кнопку, чтобы узнать подробности"
    )
    await message.answer(welcome_text, reply_markup=main_menu())

@dp.callback_query()
async def handle_callback(callback: types.CallbackQuery):
    await callback.answer()
    if callback.data == "install":
        text = (
            "📥 **Инструкция по установке и запуску Lily AI**\n\n"
            "1️⃣ **Скачай архив** по ссылке ниже:\n"
            f"📍 {DOWNLOAD_URL}\n\n"
            "2️⃣ **Распакуй архив** в любую папку на компьютере.\n\n"
            "3️⃣ **Открой Chrome** и перейди на страницу `chrome://extensions/`.\n\n"
            "4️⃣ **Включи «Режим разработчика»** (тумблер в правом верхнем углу).\n\n"
            "5️⃣ **Нажми «Загрузить распакованное расширение»** и выбери папку, куда распаковала архив.\n\n"
            "6️⃣ **Закрепи расширение** в панели браузера (иконка пазла → закрепить Lily).\n\n"
            "7️⃣ **Открой сайт Chaturbate или Stripchat** – плавающее окно Lily появится автоматически!\n\n"
            "8️⃣ **Войди в расширение**: нажми на иконку/окно, введи свой ник на сайте и нажми «Войти».\n\n"
            "9️⃣ **Готово!** Открой приватный чат (PM) и нажми «Сгенерировать ответы». Lily предложит 3 варианта.\n\n"
            "📢 **Подписывайся на новости**: @LilyAI_News"
        )
        await callback.message.edit_text(text, reply_markup=main_menu(), parse_mode="Markdown")
    elif callback.data == "faq":
        text = (
            "❓ **Часто задаваемые вопросы**\n\n"
            "**1. Расширение не видит сообщения в чате**\n"
            "→ Убедись, что ты открыла приватный чат (PM). Обнови страницу и перезагрузи расширение.\n\n"
            "**2. ИИ не использует мои смайлики**\n"
            "→ Заполни стиль в Telegram Mini App (Профиль → Настройка стиля Lily) и сохрани.\n\n"
            "**3. Как ИИ узнаёт моё имя/возраст?**\n"
            "→ Введи их в Telegram Mini App (Профиль → Личные данные).\n\n"
            "**4. Как обновить расширение?**\n"
            "→ Скачай новый архив, замени папку и перезагрузи в `chrome://extensions`\n\n"
            "**5. Где смотреть срок подписки?**\n"
            "→ Во вкладке «Профиль» Telegram Mini App.\n\n"
            "**6. Почему долгий ответ?**\n"
            "→ ИИ генерирует ответы 3-7 секунд. Если дольше — проверь интернет.\n\n"
            "**7. Есть ли пробный период?**\n"
            "→ Да, тариф START — 30 ген/день, 7 дней за $16.\n\n"
            "💡 **После оплаты тариф не активировался?** Сразу напиши в поддержку @Lily_AI_support"
        )
        await callback.message.edit_text(text, reply_markup=main_menu(), parse_mode="Markdown")
    elif callback.data == "support":
        text = (
            "💬 **Служба поддержки Lily AI**\n\n"
            "Если у тебя возникли проблемы с установкой, оплатой или работой расширения – напиши нам.\n\n"
            "📱 Telegram: @Lily_AI_support\n\n"
            "📢 Новости и обновления: @LilyAI_News"
        )
        await callback.message.answer(text, reply_markup=main_menu())
    elif callback.data == "download":
        text = f"🔗 **Ссылка на скачивание расширения Lily AI:**\n\n{DOWNLOAD_URL}\n\n📢 Подписывайся на новости: @LilyAI_News"
        await callback.message.edit_text(text, reply_markup=main_menu(), parse_mode="Markdown")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
