
# Телеграм бот для создания заметок
## Телеграм бот на питоне
Бот позволяет создавать заметки, редактировать их, удалять и просматривать список всех заметок.
## Установка
Чтобы установить программу нужно установить модули, необходимые для создания бота из requirements.txt
```
sudo apt-get update
sudo apt-get install python3
pip install -r requirements.txt
```
## Запуск на локальной машине
```
python3 main.py
```
## Описание программы
### Поддерживаемый функционал
![изображение](https://user-images.githubusercontent.com/109852961/235790483-f7cc492d-18b6-45f6-9ea4-fa21e70cc8b1.png)
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
