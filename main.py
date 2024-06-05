from config import Config
import os
import telebot, requests, random
from telebot import types 

tok = Config.TG_BOT_TOKEN

bot = telebot.TeleBot(tok)
is_bot_active = True  


@bot.message_handler(commands=["start"])
def start(message):
    private = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("✓ تلاوة ", callback_data="quran")
    buttoon = types.InlineKeyboardButton("✓ صورة دينية ", callback_data="religious")
    buttn = types.InlineKeyboardButton("خطب دينيه", callback_data="quraan")
    buttin = types.InlineKeyboardButton("الصلي علي النبي", callback_data="qurn")
    bstart = types.InlineKeyboardButton("المصحف", callback_data="starttt")
    butin = types.InlineKeyboardButton("احاديث دينية", callback_data="religiou")
    bkotob = types.InlineKeyboardButton("كتب دينية", callback_data="kotob")
    bkotobb = types.InlineKeyboardButton("اوقات الصلاة ⏱️", web_url="https://dev-almortageltech.pantheonsite.io/time")
    butteon = types.InlineKeyboardButton("مطور البوت", url="https://t.me/Almortagel_12")
    private.add(button,buttoon)
    private.add(buttin,buttn)
    private.add(bstart,butin)
    private.add(bkotob,bkotobb)
    private.add(butteon)      
    bot.send_photo(message.chat.id,text="""
✓ 👋 مرحبا بك عزيزي انا بوت اسلامي اقدم صور دينيه وتلاوات باصوات وابدعات شيوخ متعددين 
لعرض المصحف ارسل رقم الصفحة
✓ 🔍 انقر على الزر ادناة لارسال القران
""", reply_markup=private)


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
    elif call.data == "nqsbndy":
        voicesss = "https://t.me/ggcnjj/" + str(random.randint(2, 114))
        bot.send_voice(call.message.chat.id, voicesss, caption="""
✓  🌿 〈〈 صـل على سيدنا محمد 〉〉
""")
    elif call.data == "nkssd":
        voice_url = "https://t.me/telawatnader/" + str(random.randint(7, 265))
        bot.send_voice(message.chat.id, voice_url, caption="🥹♥ ¦ تـم اختيـار الشيخ عبدالباسط لـك")
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
@bot.callback_query_handler(func=lambda call: True)
def starttt(call):
    if call.data == "starttt":
       bot.send_message(message.chat.id,caption="""
مرحبا بك في قسم المصحف الرجاء ارسال رقم الصفحة لتصفح صفحات القرآن الكريم للرجوع ارسل /start
""")

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

@bot.message_handler(func=lambda message: True)
def msgs(message):
    text = message.text
    
            
print("تم تشغيل البوت اذا وقف معك شي تواصل معي @Almortagel_12")
bot.polling(none_stop=True)
"""
Dev /- @Almortagel_12
Ch /- @AlmortagelTech
In /- 2024/2/14
"""