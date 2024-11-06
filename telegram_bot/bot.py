import logging
from telegram import Update, InputMediaPhoto
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes

# Включите логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Определим состояния разговора
CITY, SQUARE, FURNITURE, DESCRIPTION, PHOTOS, DONE = range(6)

# Адрес администратора
ADMIN_CHAT_ID = 'YOUR_ADMIN_CHAT_ID'  # Замените на ID чата администратора

# Начало разговора
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Привет! В каком городе находится квартира?")
    return CITY

# Получение города
async def get_city(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['city'] = update.message.text
    await update.message.reply_text("Какова площадь квартиры в квадратных метрах?")
    return SQUARE

# Получение квадратуры
async def get_square(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['square'] = update.message.text
    await update.message.reply_text("Есть ли мебель и техника? (Да/Нет)")
    return FURNITURE

# Получение информации о мебели
async def get_furniture(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['furniture'] = update.message.text
    await update.message.reply_text("Пожалуйста, дайте описание квартиры.")
    return DESCRIPTION

# Получение описания квартиры
async def get_description(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['description'] = update.message.text
    await update.message.reply_text("Отправьте фотографии квартиры (можно несколько). Чтобы закончить, введите /done.")
    return PHOTOS

# Получение фотографий
async def get_photos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.photo:
        # Добавляем фотографию в список
        if 'photos' not in context.user_data:
            context.user_data['photos'] = []
        context.user_data['photos'].append(update.message.photo[-1].file_id)
        await update.message.reply_text("Фотография получена! Если есть еще фотографии, отправьте их. Чтобы закончить, введите /done.")
        return PHOTOS  # Остаемся в том же состоянии, чтобы принимать больше фотографий

    await update.message.reply_text("Пожалуйста, отправьте фотографии квартиры.")
    return PHOTOS

# Завершение процесса получения фотографий
async def done(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if 'photos' in context.user_data:
        await send_to_admin(context, context.user_data)
    else:
        await update.message.reply_text("Фотографии не были отправлены.")

    await update.message.reply_text("Ваше объявление отправлено администратору!")
    return ConversationHandler.END

# Отправка данных администратору
async def send_to_admin(context, data):
    message = (
        f"Новое объявление о сдаче квартиры:\n"
        f"Город: {data['city']}\n"
        f"Площадь: {data['square']} кв.м\n"
        f"Мебель и техника: {data['furniture']}\n"
        f"Описание: {data['description']}\n"
    )

    # Отправляем сообщение и фото (если есть) администратору
    if 'photos' in data:
        media = [InputMediaPhoto(media=photo) for photo in data['photos']]
        await context.bot.send_media_group(chat_id=ADMIN_CHAT_ID, media=media)

    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=message)

# Завершение разговора
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Объявление отменено.")
    return ConversationHandler.END

def main() -> None:
    # Используем Application.builder() вместо Updater для создания приложения
    application = Application.builder().token("7500486461:AAEUd1T5Rz1MTKCpv0ZoelN5EVhWG52FxG4").build()  # Замените на ваш токен

    # Настройка разговорного обработчика
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_city)],
            SQUARE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_square)],
            FURNITURE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_furniture)],
            DESCRIPTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_description)],
            PHOTOS: [MessageHandler(filters.PHOTO, get_photos)],
            DONE: [CommandHandler('done', done)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Регистрация обработчиков
    application.add_handler(conv_handler)

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
