import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from app.config import config
import cryptography.ent as ent  # Імпортуємо твій файл

# Ініціалізація бота і диспетчера
bot = Bot(token=config.BOT_TOKEN.get_secret_value())
dp = Dispatcher()


# --- Handlers ---

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "👋 Привіт! Я CryptoMath Bot.\n"
        "Я вмію рахувати НСД, шукати обернені елементи та генерувати прості числа.\n\n"
        "Спробуй: /gcd 1071 462"
    )


@dp.message(Command("gcd"))
async def cmd_gcd(message: Message):
    """
    Рахує НСД двох чисел.
    Використання: /gcd <a> <b>
    """
    try:
        # Розбираємо аргументи
        parts = message.text.split()
        if len(parts) != 3:
            await message.answer("❌ Формат: /gcd <число_a> <число_b>")
            return

        a = int(parts[1])
        b = int(parts[2])

        # 🔥 Виконуємо синхронну функцію в окремому потоці,
        # щоб не блокувати бота
        result = await asyncio.to_thread(ent.gcd, a, b)

        await message.answer(f"✅ GCD({a}, {b}) = <b>{result}</b>", parse_mode="HTML")

    except ValueError:
        await message.answer("❌ Будь ласка, введи цілі числа.")
    except Exception as e:
        await message.answer(f"❌ Сталася помилка: {str(e)}")


@dp.message(Command("gen_prime"))
async def cmd_gen_prime(message: Message):
    """
    Генерує псевдопросте число заданої довжини.
    Використання: /gen_prime <bits>
    """
    try:
        parts = message.text.split()
        n = int(parts[1]) if len(parts) > 1 else 100  # Дефолт 100

        await message.answer("⏳ Генерую число, зачекайте...")

        # Це важка функція, обов'язково в окремий потік
        # У твоєму ent.py функція називається strong_peseudoPrime_generator
        # (до речі, там помилка в слові pseudo, але використовуємо як є)
        prime_num = await asyncio.to_thread(ent.strong_peseudoPrime_generator, n, 10)

        await message.answer(f"🎲 Згенероване число:\n<code>{prime_num}</code>", parse_mode="HTML")

    except ValueError:
        await message.answer("❌ Введи коректну довжину.")