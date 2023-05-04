import sys
sys.path.insert(1, './src')
from Globals import *

import telebot;
from telebot import types;
bot = telebot.TeleBot(api_label)

name = '';
reg = False;
note_dict = {}
curname = '';
text = '';

@bot.message_handler(commands=['reg'])
def register(message):
    """ Registration for usage of the bot. """
    if (checkreg()):
        bot.send_message(message.from_user.id, change_name_log)    
    bot.send_message(message.from_user.id, ask_name_log);
    bot.register_next_step_handler(message, get_name);

def get_name(message): 
    global name
    name = message.text
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text=yes_log, callback_data=yes_eng) 
    keyboard.add(key_yes) 
    key_no= types.InlineKeyboardButton(text=no_log, callback_data=no_eng)
    keyboard.add(key_no)
    question = your_name_log + name + ques_mark
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    
@bot.message_handler(commands=['view_note'])
def view_note(message):
    """ Viewing the note. """
    if (not checkreg()):
        bot.send_message(message.from_user.id, first_reg_log)
    else:
        bot.send_message(message.from_user.id, view_note_log)
        bot.register_next_step_handler(message, view_note);

@bot.message_handler(commands=['view_note_list'])
def view_note_list(message):
    """ The list of note names. """
    if (not checkreg()):
        bot.send_message(message.from_user.id, first_reg_log)
    else:
        ss = name_list_log
        for k in note_dict.keys():
            ss += k + '\n'
        bot.send_message(message.from_user.id, ss)
        
def view_note(message):
    global curname
    curname = message.text
    if curname == back_log:
        bot.send_message(message.from_user.id, cancellation);
        return
    if curname not in note_dict.keys():
        bot.send_message(message.from_user.id, does_not_exist_log)
        bot.register_next_step_handler(message, view_note)
    else:
        bot.send_message(message.from_user.id, note_dict[curname])

@bot.message_handler(commands=['delete_note'])
def delete_note(message):
    """ Deletion of the note. """
    if (not checkreg()):
        bot.send_message(message.from_user.id, first_reg_log)
    else:
        bot.send_message(message.from_user.id, delete_note_log)
        bot.register_next_step_handler(message, enter_delete_name)

def enter_delete_name(message):
    global curname
    curname = message.text
    if curname == back_log:
        bot.send_message(message.from_user.id, cancellation);
    return
    if curname not in note_dict.keys():
        bot.send_message(message.from_user.id, does_not_exist_log)
        bot.register_next_step_handler(message, enter_delete_name)
    else:
        note_dict.pop(curname)
        print(note_dict)
        bot.send_message(message.from_user.id, deleted_log)
        
@bot.message_handler(commands=['edit_note'])
def edit_note(message):
    """ Editing of an existing note. """
    if (not checkreg()):
        bot.send_message(message.from_user.id, first_reg_log)
    else:
        bot.send_message(message.from_user.id, editing_note_log)
        bot.register_next_step_handler(message, edit_note_name)

def edit_note_name(message):
    global curname;
    curname = message.text
    if curname == back_log:
        bot.send_message(message.from_user.id, cancellation);
        return
    if curname not in note_dict.keys():
        bot.send_message(message.from_user.id, does_not_exist_log)
        bot.register_next_step_handler(message, edit_note_name);
    else:
        bot.send_message(message.from_user.id, enter_text_log + curname + ":")
        bot.register_next_step_handler(message, edit_given_note)

def edit_given_note(message):
    global text
    text = message.text
    if text == back_log:
        bot.send_message(message.from_user.id, cancellation);
        return
    global curname;
    note_dict[curname] = text
    print(note_dict)
    bot.send_message(message.from_user.id, written)
    
@bot.message_handler(commands=['add_note'])
def add_note(message):
    """ Adding a note to the list of notes. """
    if (not checkreg()):
        bot.send_message(message.from_user.id, first_reg_log)
    else:
        bot.send_message(message.from_user.id, new_creation_log)
        bot.register_next_step_handler(message, enter_note_name)

def enter_note_name(message):
    global curname;
    curname = message.text
    print(curname, back_log)
    if curname == back_log:
        bot.send_message(message.from_user.id, cancellation);
        return
    if curname in note_dict.keys():
        bot.send_message(message.from_user.id, already_exists_log)
        bot.register_next_step_handler(message, enter_note_name);
    else:
        bot.send_message(message.from_user.id, unique_name_and_enter_log)
        bot.register_next_step_handler(message, insert_into_body)

def insert_into_body(message):
    global text;
    text = message.text
    if text == back_log:
        bot.send_message(message.from_user.id, cancellation);
        return
    global curname;
    note_dict[curname] = text
    print(note_dict)
    bot.send_message(message.from_user.id, written)
    
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    """ Pop-up 'yes' and 'no' buttons. """
    if call.data == yes_eng: 
        set_reg_true()
        bot.send_message(call.message.chat.id, name_saved);
    elif call.data == no_eng:
        set_reg_false()
        bot.send_message(call.message.chat.id, writereg)

def set_reg_true():
    global reg;
    reg = True

def set_reg_false():
    global reg;
    reg = True

def checkreg():
    global reg;
    return reg
@bot.message_handler(commands=['start', 'help'])
def start(message):
    """ Trivia about the abilities of the bot. """
    bot.send_message(message.from_user.id, description_log);
    
bot.polling(none_stop=True, interval=0)
