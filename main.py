import telebot
from telebot import types

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

# Ваш ID для получения уведомлений
ADMIN_ID = 123456789  # Замените на ваш ID

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Отправляем автоматический ответ
    bot.reply_to(message, "Привет! Я бот. Спасибо, что запустили меня!")

    # Получаем информацию о пользователе
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    # Получаем аватарку пользователя
    user_profile_photos = bot.get_user_profile_photos(user_id)
    if user_profile_photos.photos:
        # Берем первую фотографию (самую последнюю)
        photo = user_profile_photos.photos[0][-1].file_id
        photo_url = f"https://api.telegram.org/file/bot{bot.token}/{bot.get_file(photo).file_path}"
    else:
        photo_url = "Аватарки нет"

    # Формируем сообщение для админа
    admin_message = (
        f"Кто-то нажал /start:\n"
        f"ID: {user_id}\n"
        f"Имя: {first_name} {last_name}\n"
        f"Ник: @{username}\n"
        f"Аватарка: {photo_url}"
    )

    # Отправляем сообщение админу
    bot.send_message(ADMIN_ID, admin_message)

# Запуск бота
bot.polling(none_stop=True)
