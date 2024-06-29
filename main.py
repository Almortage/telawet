import telebot, requests, random, re 
from config import Config
from telebot import types 
import os
import telebot
import random
import requests
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup


token = Config.TG_BOT_TOKEN#توكنك
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    name = message.from_user.first_name
    message_text = f"""اهلاً〘 {name} 〙.
انا بوت اسلامي
اذا اردت بايو ديني اكتب ﹛بايو ديني ﹜.
اذا اردت شي اضغط علي الازرار"""
    keyboard = [[InlineKeyboardButton("- المطور .", url=f"https://t.me/Almortagel_12"),
    InlineKeyboardButton("✓ تلاوة ", callback_data="quran")]
    [InlineKeyboardButton("✓ صورة دينية ", callback_data="religious"),
    InlineKeyboardButton("كتب دينية", callback_data="kotob")]
    [InlineKeyboardButton("احاديث دينية", callback_data="religiou"),
    types.InlineKeyboardButton("الصلي علي النبي", callback_data="qurn")]
    [InlineKeyboardButton("✓ صورة دينية ", callback_data="religious")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=message.chat.id, text=message_text, reply_markup=reply_markup)





@bot.callback_query_handler(func=lambda call: True)
def tylaoa(call):
    if call.data == "quran":
        voices = "https://t.me/ALMORTAGELRSK/" + str(random.randint(7, 276))
        bot.send_voice(call.message.chat.id, voices, caption="""
✓  🌿 〈〈 صـل على سيدنا محمد 〉〉
""")
    elif call.data == "religious":
        voicees = "https://t.me/livequrann/" + str(random.randint(22, 221))
        bot.send_photo(call.message.chat.id, voicees, caption="""
✓  🌿 〈〈 صـل على سيدنا محمد 〉〉
""")
    elif call.data == "quraan":
        voicess = "https://t.me/fresdewi/" + str(random.randint(2, 201))
        bot.send_voice(call.message.chat.id, voicess, caption="""
✓  🌿 〈〈 صـل على سيدنا محمد 〉〉
""")
    elif call.data == "religiou":
        voice = "https://t.me/dmatrix12/" + str(random.randint(799, 1341))
        bot.send_photo(call.message.chat.id, voice, caption="""
✓  🌿 〈〈 صـل على سيدنا محمد 〉〉
""")
    elif call.data == "kotob":
        voic = "https://t.me/kotobeslameah/" + str(random.randint(2, 1950))
        bot.send_document(call.message.chat.id, voic, caption="""
 تم اختيار هذا الكتاب لك
""")
    elif call.data == "qurn":
        voics = ["اللهم صلي علي سيدنا ونبينا محمد",]
        bot.send_message(call.message.chat.id, voics)
    
    elif call.data == "starttt":
        voic = ["مرحبا بك في قسم المصحف الرجاء ارسال رقم الصفحة لتصفح صفحات القرآن الكريم للرجوع ارسل /start",]
        bot.send_message(call.message.chat.id,voic)
@bot.message_handler(func=lambda message: True)
def all(message):
    try:
            num = int(message.text)
            url = "https://quran.ksu.edu.sa/png_big/" + str(num) + ".png"

            keyboard = types.InlineKeyboardMarkup()
            cou = types.InlineKeyboardButton(text=f"• {num} •", callback_data="couu")
            previous = types.InlineKeyboardButton(text="صفحة السابقة", callback_data=str(num - 1))
            next = types.InlineKeyboardButton(text="صفحة التالية", callback_data=str(num + 1))

            keyboard.row(cou)
            keyboard.row(previous,next)

            bot.send_photo(message.chat.id,url, reply_markup=keyboard)
    except:
            pass
            bot.reply_to(message,'error')

@bot.callback_query_handler(func=lambda call: True)
def alll(call):
    if call.data == 'couu':
     bot.answer_callback_query(call.id, text='هذا زر يعرض فيه العدد فقط')
     exit()
    num = int(call.data)
    url = "https://quran.ksu.edu.sa/png_big/" + str(num) + ".png"

    keyboard = types.InlineKeyboardMarkup()

    cou = types.InlineKeyboardButton(text=f"• {num} •", callback_data="couu")
    previous = types.InlineKeyboardButton(text="صفحة السابقة", callback_data=str(num - 1))
    next = types.InlineKeyboardButton(text="صفحة التالية", callback_data=str(num + 1))


    keyboard.row(cou)
    keyboard.row(previous,next)

    bot.edit_message_media(types.InputMediaPhoto(url), call.message.chat.id, call.message.message_id,reply_markup=keyboard)
print("@Almortagel_12")
print("\033[1;33m• Running..... /start ")
bot.polling(none_stop=True)


print("""اشتغل البوت هسه روح للبوت مالك اكتب /start
اي مشكلة تواجهك بلبوت تعال راسلني تلكرام
حسابي : dudrd""")
bot.polling()
