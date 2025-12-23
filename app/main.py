from fastapi import FastAPI
from contextlib import asynccontextmanager
import asyncio
from app.config import config
from app.bot import bot, dp
from aiogram.types import Update


# Життєвий цикл додатку
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Дії при старті
    if config.RUN_MODE == "webhook":
        # Тут буде логіка налаштування вебхука для продакшена
        webhook_url = f"{config.WEBHOOK_URL}/webhook"
        await bot.set_webhook(webhook_url)
    else:
        # Для локальної розробки (Polling)
        # Запускаємо poling у фоновому завданні
        asyncio.create_task(dp.start_polling(bot))

    yield  # Тут додаток працює

    # Дії при зупинці
    if config.Config.RUN_MODE == "webhook":
        await bot.delete_webhook()


app = FastAPI(lifespan=lifespan)


# Ендпоінт для Telegram Webhook (для продакшена)
@app.post("/webhook")
async def webhook_endpoint(update: dict):
    telegram_update = Update.model_validate(update, context={"bot": bot})
    await dp.feed_update(bot, telegram_update)
    return {"status": "ok"}


@app.get("/")
async def health_check():
    return {"status":"running", "mode": config.Config.RUN_MODE}