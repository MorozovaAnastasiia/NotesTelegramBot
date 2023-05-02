# Телеграм бот для создания заметок
## Телеграм бот на питоне
Бот позволяет создавать заметки, редактировать их, удалять и просматривать список всех заметок.
## Установка
Чтобы установить программу нужно установить модуль telebot
## Запуск на локальной машине
```
python3 bot.py
```
## Описание программы
### Поддерживаемый функционал
- Напишите /reg, чтобы зарегестрироваться (это обязательно для использования бота, нужно просто ввести свой ник)
- /add_note чтобы добавить заметку
Сначала введите название заметки, а потом ее содержание
- /delete_note чтобы удалить заметку
Введите название заметки, которую хотите удалить
- /edit_note чтобы редактировать заметку
Введите название заметки, которую хотите отредактировать
- /view_note_list чтобы посмотреть список заметок
- /view_note чтобы посмотреть заметку
Введите название заметки, которую хотите посмотреть
- /back чтобы отменить последнее действие
Это можно сделать на любом шаге, кроме регистрации (потому что это обязательно для использования бота)
