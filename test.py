
from datetime import date
import telebot
import random
import os
from telebot import types
from time import sleep
from tabulate import tabulate
import sqlite3
import threading
import json
try:os.chdir('/root/LotteryBot/')
except:pass
today_raw = date.today()
today = today_raw.strftime("%d%m%Y")
#clear keyboard
clear_key = types.ReplyKeyboardRemove(selective=False)
db_path='LotteryBot.db'

# main screen button
bot = telebot.TeleBot("1032035380:AAH_SyevPLSKg80LKg5-CBfXie1-iNL4MNY")
back = types.KeyboardButton("חזור אחורה")
canceled = types.KeyboardButton("ביטול")

backtoadmin= types.InlineKeyboardMarkup()
backtoadmin.add(types.InlineKeyboardButton('<<חזור', callback_data="backtoadminhome"))

close = types.InlineKeyboardMarkup()
close.add(types.InlineKeyboardButton(
"🚫 סגור", callback_data="closeabout"))

#####Admin Buttons
admin_home = types.InlineKeyboardMarkup()
admin_home.add(types.InlineKeyboardButton("➗ הוסף משתמש להגרלה ➕", callback_data="Add_user"))
admin_home.add(types.InlineKeyboardButton("➖מחק משתמש מן ההגרלה ➖", callback_data="Delete_User"))
admin_home.add(types.InlineKeyboardButton(" הגדר מס' זוכים ", callback_data="number_of_winner"))
admin_home.add(types.InlineKeyboardButton(" 🎉 זוכי ההגרלה 🎉", callback_data="show_winner_list"))
admin_home.add(types.InlineKeyboardButton("▶️ התחל הגרלה ", callback_data="Start_lottery"))
admin_home.add(types.InlineKeyboardButton(" שליחת הודעות למנויים 📨", callback_data="messenger"))

homekey = admin_home
send_review = '''
SELECT * FROM reviews WHERE token ='%s' ORDER BY last_review DESC
'''

# cancel button

cancel_key = types.InlineKeyboardMarkup()
cancel_key.add(types.InlineKeyboardButton("❌ביטול ❌", callback_data="CANCEL"))

#back and cancel
cancel_key_board = types.ReplyKeyboardMarkup(row_width=2)

cancel = types.KeyboardButton("ביטול")
cancel_key_board.add(
back,
cancel)

# INSERT QUERY
insert_review = '''
INSERT INTO reviews (dealer,telegram_user,location1,location2,delear_response,cost,service_Rating,Quality_rating,Realiablity_Rating,Comments,last_Review,approve,token)
VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',%s,%s,%s)
'''
# get Query

# reviews by this user
get_this_user_reviews = '''
SELECT * FROM reviews WHERE dealer ='%s' and telegram_user ='%s' and approve=1 ORDER BY last_review DESC
'''
# reviews for this dealer
get_reviews = '''
SELECT * FROM reviews WHERE dealer ='%s' and approve=1 ORDER BY last_review DESC
'''
# reviews by user
user_reviews = '''
SELECT * FROM reviews WHERE telegram_user ='%s' AND approve=1 ORDER BY last_review DESC
'''
# balance review for this dealer today
get_this_user_balance_reviews = '''
SELECT * FROM reviews WHERE dealer ='%s' and telegram_user ='%s' and last_review='%s' ORDER BY last_review DESC
'''
# balance review today
get_this_user_Balance_reviews_today = '''
SELECT * FROM reviews WHERE telegram_user ='%s' and last_review='%s' ORDER BY last_review DESC
'''

#approval-update:
approval_q='''UPDATE reviews SET approve=%s WHERE token=%s'''


create_user = '''INSERT INTO user (username,winner,token) VALUES (
'%s',
'0',
%s
); '''
remove_dealer_q = '''DELETE FROM user WHERE username='%s' '''

get_all_users='''SELECT id,username from user WHERE winner=0'''

admins = ['Muruganandham1998','yaronlondon234']

####Manager panel
@bot.message_handler(commands=['manager'])
def add_admin(message,*args):
if message.from_user.username in admins:
conn = sqlite3.connect(db_path)
cursor = conn.execute('''CREATE TABLE IF NOT EXISTS `adminslist` (
`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
`username` TEXT NOT NULL UNIQUE)''')
conn.commit()
cursor = conn.execute('''SELECT username FROM adminslist''')
all_channels = cursor.fetchall()
print(all_channels)
buttonsAdmin= types.InlineKeyboardMarkup()
for x in all_channels:
buttonsAdmin.add(types.InlineKeyboardButton(x[0], url=f'''t.me/{x[0]}'''),types.InlineKeyboardButton('❌', callback_data='reMoveFromAdmin_%s'%x[0]))
buttonsAdmin.add(types.InlineKeyboardButton('ADD admin', callback_data="AdminListAdd"))
buttonsAdmin.add(types.InlineKeyboardButton('<<חזור', callback_data="ClOse"))
msg=bot.send_message(message.from_user.id,'Manage Admin',reply_markup=buttonsAdmin)
else:
msg=bot.send_message(message.from_user.id,'Your are not manager',reply_markup=buttonsAdmin)


@bot.message_handler(commands=['admin'])
def admin_start(message):
try:
if message.from_user.username in admins:
bot.delete_message(message.chat.id, message.message_id)
msg = bot.send_message(message.from_user.id, '''Hi Admin''' ,reply_markup=admin_home)
else:
msg = bot.send_message(message.from_user.id, '''Not admin''' )
except Exception as e:
bot.send_message(110663594, '%s,%s'%(e,0))
print(e)
pass
###Message handele
def send_message_handler(message,message_text='No Text',handler=None,button=cancel_key):
try:
msg=bot.send_message(message.message.chat.id,message_text,reply_markup=button)
if handler != None:
bot.register_next_step_handler(msg, handler, msg)

except Exception as e:
bot.send_message(110663594, '%s,%s'%(e,2))
print(e)
pass
######token generator
def token_generator():
flag=True
while flag:
token=random.randint(1000,100000)
conn = sqlite3.connect(db_path)
cursor = conn.execute('''SELECT COUNT(1) FROM user WHERE token =%s ''' % (token))
if cursor.fetchone()[0] == 0:
flag=False
return token

###render all list
def send_list_to_remove(message):
try:
conn = sqlite3.connect(db_path)
cursor = conn.execute(get_all_users)
all_user = cursor.fetchall()
print(all_user)
admin_keys1= types.InlineKeyboardMarkup()
for x in all_user:
admin_keys1.add(types.InlineKeyboardButton('remove >> %s'%x[1], callback_data=f"Ruser_{x[0]}"))
admin_keys1.add(types.InlineKeyboardButton('<<חזור', callback_data="backtoadminhome"))
try:msg=bot.edit_message_text('Mangement panel',chat_id=message.message.chat.id,message_id=message.message.message_id,reply_markup=admin_keys1)
except:pass
except Exception as e:
bot.send_message(110663594, '%s,%s'%(e,3))
print(e)
pass

def send_remove_user(message):
try:
conn = sqlite3.connect(db_path)
cursor = conn.execute(get_all_users)
all_user = cursor.fetchall()
print(all_user)
admin_keys1= types.InlineKeyboardMarkup()
for x in all_user:
admin_keys1.add(types.InlineKeyboardButton('remove >> %s'%x[1], callback_data=f"Ruser_{x[0]}"))
admin_keys1.add(types.InlineKeyboardButton('<<חזור', callback_data="backtoadminhome"))
try:msg=bot.edit_message_text('hi',chat_id=message.message.chat.id,message_id=message.message.message_id,reply_markup=admin_keys1)
except:pass
except Exception as e:
bot.send_message(110663594, '%s,%s'%(e,3))
print(e)
pass

def saveUser(message,*args):
try:
msg=args[0]
try:delete=bot.delete_message(chat_id=message.chat.id,message_id=message.message_id)
except:pass
conn = sqlite3.connect(db_path)
cursor = conn.execute('''SELECT COUNT(1) FROM user WHERE username ='%s' ''' % (message.text.replace('@','')))
if not cursor.fetchone()[0]:
conn = sqlite3.connect(db_path)
conn.execute(create_user%(message.text.replace('@',''),token_generator()))
conn.commit()
try:
msg=bot.edit_message_text('User Added',chat_id=msg.chat.id,message_id=msg.message_id,reply_markup=admin_home)
except:
pass
else:
msg=bot.edit_message_text('User Exists',chat_id=msg.chat.id,message_id=msg.message_id,reply_markup=cancel_key)
bot.register_next_step_handler(msg, saveUser, msg)

except Exception as e:
bot.send_message(110663594, '%s,%s'%(e,5))
print(e)
pass

def number_of_winner(message,*args):
try:
if message.content_type=='text' and (message.text).isdigit():
msg=args[0]
delete=bot.delete_message(chat_id=message.chat.id,message_id=message.message_id)
conn = sqlite3.connect(db_path)
conn.execute(f'''UPDATE temp SET value={int(message.text)} WHERE key='winner_count' ''')
conn.commit()
try:
msg=bot.edit_message_text('Winner Count Updated',chat_id=msg.chat.id,message_id=msg.message_id,reply_markup=admin_home)
except:
pass
else:
msg=bot.edit_message_text('Enter a Integer',chat_id=msg.chat.id,message_id=msg.message_id,reply_markup=cancel_key)
bot.register_next_step_handler(msg, saveUser, msg)

except Exception as e:
bot.send_message(110663594, '%s,%s'%(e,5))
print(e)
pass

def multi_threading(function):
def decorator(*args, **kwargs):
t = threading.Thread(target = function, args=args, kwargs=kwargs)
t.daemon = True
t.start()
return decorator

@multi_threading
def lotery_count(chat_id=00,):
clock=["🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙",]
animation=["🔴",'🔵']
try:
lottery_message=bot.send_message(chat_id,'''
🔴🔴🔴🔴🔴LOTTERY COUNTDOWN BEGINS🔴🔴🔴🔴''')
for count in range(0,9):
print(count)
lottery_message=bot.edit_message_text(chat_id=lottery_message.chat.id,message_id=lottery_message.message_id,text=f'''
{animation[count%2]*5}LOTTERY COUNTDOWN BEGINS{animation[count%2]*5}
{clock[count]*5} {count+1} {clock[count]*5}''')
sleep(0.7)
except:
print("Invalid Chat id")

finally:
try:bot.delete_message(lottery_message.chat.id,lottery_message.message_id)
except:print('Invalid chat')

@multi_threading
def batch_message(chat_id,winner_text=''):
try:
bot.send_message(chat_id,text=f'''
🚥🚥🚥Winners Are 🚥🚥🚥
{winner_text}
''')
except:
print('Invalid Chat id')

def start_lottery(message,*args):
try:bot.delete_message(message.message.chat.id,message.message.message_id)
except:pass
clock=["🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙",]
animation=["🔴",'🔵']
conn = sqlite3.connect(db_path)
# cursor = conn.execute('''SELECT id FROM user WHERE start=1 ''')
cursor = conn.execute('''SELECT chat_id FROM user WHERE start=1 ''')
users_in_game_chat_id = cursor.fetchall()
conn.close()
for user in users_in_game_chat_id:
lotery_count(user[0])

lottery_message=bot.send_message(message.from_user.id,'''
🔴🔴🔴🔴🔴LOTTERY COUNTDOWN BEGINS🔴🔴🔴🔴''')

for count in range(0,9):
print(count)
lottery_message=bot.edit_message_text(chat_id=lottery_message.chat.id,message_id=lottery_message.message_id,text=f'''
{animation[count%2]*5}LOTTERY COUNTDOWN BEGINS{animation[count%2]*5}
{clock[count]*5} {count+1} {clock[count]*5}''')
sleep(0.7)
conn = sqlite3.connect(db_path)
cursor = conn.execute('''SELECT Value FROM temp WHERE key='winner_count' ''')
winner_count = cursor.fetchall()[0][0]
conn.close()
conn = sqlite3.connect(db_path)
# cursor = conn.execute('''SELECT id FROM user WHERE start=1 ''')
cursor = conn.execute('''SELECT id,username,token FROM user WHERE start=1 ''')
users_in_game = cursor.fetchall()
conn.close()
winners_list=[]
winner_text=''
for x in range(int(winner_count)+10):
winners_list.append(random.randint(0,len(users_in_game)-1))
print(winners_list)
winners_list=list(set(winners_list))
random.shuffle(winners_list)
print(winners_list)
winners_list=winners_list[0:int(winner_count)]
print(winners_list)
conn = sqlite3.connect(db_path)
conn.execute(f''' DELETE FROM user WHERE start=3 ''')
conn.commit()
conn.execute(f''' UPDATE user SET winner=0 ''')
conn.commit()
conn.close()
for winner in winners_list:
conn = sqlite3.connect(db_path)
conn.execute(f'''UPDATE user SET winner=1,start=3,username="@{users_in_game[winner][1]}" WHERE id={int(users_in_game[winner][0])} ''')
conn.commit()
conn.close()
winner_text=f'''{winner_text}
✅ @{users_in_game[winner][1]} 🗞 Lottery Code: {users_in_game[winner][2]}'''
###For all user
for user in users_in_game_chat_id:
batch_message(user[0],winner_text)

lottery_message=bot.edit_message_text(chat_id=lottery_message.chat.id,message_id=lottery_message.message_id,text=f'''
🚥🚥🚥Winners Are 🚥🚥🚥
{winner_text}
''',reply_markup=backtoadmin)
conn = sqlite3.connect(db_path)
conn.execute(f'''DELETE FROM user WHERE NOT winner=1 ''')
conn.commit()
conn.execute(f'''DELETE FROM user_dump ''')
conn.commit()
conn.close()


def send_message_winners(message,*args):
try:
msg=args[0]
try:bot.delete_message(msg.chat.id,msg.message_id)
except:pass
try:bot.delete_message(message.chat.id,message.message_id)
except:pass
conn = sqlite3.connect(db_path)
cursor = conn.execute('''SELECT chat_id FROM user WHERE winner=1 ''')
winner_list = cursor.fetchall()
for user in winner_list:
try:msg=bot.send_message(user[0],str(message.text))
except:print(user[0],'Text: ',str(message.text))
msg=bot.send_message(message.from_user.id,'Message Send to all Winners',reply_markup=close)
except Exception as e:
bot.send_message(110663594, str(e)+"2")
print(e)

def send_message_channel(message,*args):
try:
msg=args[0]
try:bot.delete_message(msg.chat.id,msg.message_id)
except:pass
try:bot.delete_message(message.chat.id,message.message_id)
except:pass
channel=['110663594']
for user in channel:
try:msg=bot.send_message(user,str(message.text))
except:print(user,'Text: ',str(message.text))
msg=bot.send_message(message.from_user.id,'Message Send to all channel',reply_markup=close)
except Exception as e:
bot.send_message(110663594, str(e)+"send_message_channel")
print(e)
def send_message_user(message,*args):
try:
msg=args[0]
try:bot.delete_message(msg.chat.id,msg.message_id)
except:pass
try:bot.delete_message(message.chat.id,message.message_id)
except:pass
conn = sqlite3.connect(db_path)
cursor = conn.execute('''SELECT chat_id FROM user_dump ''')
winner_list = cursor.fetchall()
for user in winner_list:
try:msg=bot.send_message(user[0],str(message.text))
except:print(user[0],'Text: ',str(message.text))
msg=bot.send_message(message.from_user.id,'Message Send to all user',reply_markup=close)
except Exception as e:
bot.send_message(110663594, str(e)+"2")
print(e)

@bot.message_handler(regexp='hi')
@bot.message_handler(commands=['start'])
def send_welcome(message):
try:
conn = sqlite3.connect(db_path)
cursor = conn.execute('''SELECT COUNT(1) FROM user WHERE username ='%s' ''' % (message.from_user.username))
cursor2 = conn.execute('''SELECT COUNT(1) FROM user_dump WHERE username ='%s' ''' % (message.from_user.username))
if not cursor2.fetchone()[0]:
conn.execute(f'''INSERT INTO user_dump ("username", "chat_id") VALUES ('{str(message.from_user.username)}',{message.from_user.id} ) ''')
conn.commit()
if cursor.fetchone()[0]:
conn.execute(f"""UPDATE user SET chat_id={message.from_user.id}, start=1 WHERE username='{message.from_user.username}' """)
conn.commit()
cursor = conn.execute('''SELECT token FROM user WHERE username ='%s' ''' % (message.from_user.username))
user_detail=cursor.fetchone()
bot.send_message(message.from_user.id, f''' Hi Your lottery code is {user_detail[0]}''')
conn.close()

except Exception as e:
bot.send_message(110663594, str(e)+"2")
print(e)


@bot.callback_query_handler(func=lambda call: True)
def test_callback(message):
try:
print('call:', message.data)
if message.data == 'Add_user':
try:
try:delete=bot.delete_message(chat_id=message.message.chat.id,message_id=message.message.message_id)
except:pass
msg=bot.send_message(message.message.chat.id,'Enter the Username',reply_markup=cancel_key)
bot.register_next_step_handler(msg, saveUser, msg)

except Exception as e:
bot.send_message(110663594, '%s,%s'%(e,2))
print(e)
pass
elif message.data=='Delete_User':
send_list_to_remove(message)
elif message.data=='number_of_winner':
conn = sqlite3.connect(db_path)
cursor = conn.execute('''SELECT value FROM temp WHERE key='winner_count' ''')
winner_count = cursor.fetchall()[0][0]

send_message_handler(message,message_text=f'''Winner Count:{winner_count}
Enter the new Number of Winners ''',handler=number_of_winner,button=close)

elif message.data=='show_winner_list':
conn = sqlite3.connect(db_path)
cursor = conn.execute('''SELECT username FROM user WHERE winner=1 ''')
winners = cursor.fetchall()
winner_list_text=''
for winner in winners:
winner_list_text=f"""{winner_list_text}
👨🏻‍💼>> {winner[0]} """

print(winner_list_text)
send_message_handler(message,message_text=f'''🎉🎊🎁WINNERS🎁🎊🎉
{winner_list_text}''',handler=None,button=close)

elif str(message.data).startswith('Ruser'):
details=str(message.data).split('_')
pk_user=int(details[1])
conn = sqlite3.connect(db_path)
conn.execute(f'''DELETE from user where id={pk_user} ''')
conn.commit()
conn.close()
bot.answer_callback_query(callback_query_id=message.id,text='User Removed')
send_list_to_remove(message)
elif message.data=='Start_lottery':
conn = sqlite3.connect(db_path)
cursor = conn.execute('''SELECT COUNT(1) FROM user WHERE start =1 ''')
if int(cursor.fetchone()[0]) > 10:
start_lottery(message)
else:
bot.answer_callback_query(callback_query_id=message.id,text='There must me more than 10 user would get lottery')


elif message.data=='messenger':
messenger = types.InlineKeyboardMarkup()
messenger.add(types.InlineKeyboardButton("Send Message To winners", callback_data="send_message_winners"))
messenger.add(types.InlineKeyboardButton("Send Message To Channel", callback_data="send_message_Channel"))
messenger.add(types.InlineKeyboardButton("Send Message To current users", callback_data="send_message_users"))
messenger.add(types.InlineKeyboardButton('<<חזור', callback_data="backtoadminhome"))
bot.edit_message_text(text='Messenger',chat_id=message.message.chat.id,message_id=message.message.message_id,reply_markup=messenger)
elif message.data=='send_message_winners':
send_message_handler(message,message_text='Enter the message to be sent',handler=send_message_winners)
elif message.data=='send_message_Channel':
send_message_handler(message,message_text='Enter the message to be Channel',handler=send_message_channel)
elif message.data=='send_message_users':
send_message_handler(message,message_text='Enter the message to be user',handler=send_message_user)

elif message.data == "CANCEL":
print('cancel')
cancel(message)
elif message.data == "closeabout":
try:bot.clear_step_handler_by_chat_id(message.from_user.id)
except:pass
try:bot.delete_message(message.message.chat.id,message.message.message_id)
except:pass
elif message.data == 'backtoadminhome':
bot.edit_message_text(text='Management Panel',chat_id=message.message.chat.id,message_id=message.message.message_id,reply_markup=admin_home)


except Exception as e:
bot.send_message(110663594, str(e)+"29")
print(e)
pass


def cancel(message):
try:
markup = types.ReplyKeyboardRemove(selective=False)

try:
print('in try cancel')
bot.delete_message(message.message.chat.id,
message.message.message_id)
pass
except:
print('in exc cancel')
try:
bot.delete_message(message.chat.id, message.message_id)
except:
pass
pass
delete = bot.send_message(message.from_user.id,
("__________________"), reply_markup=markup)
bot.delete_message(delete.chat.id, delete.message_id)
msg = bot.send_message(message.from_user.id, ''' ''', reply_markup=homekey)
bot.clear_step_handler_by_chat_id(message.from_user.id)
except Exception as e:
bot.send_message(110663594, str(e)+"33")
print(e)
pass


try:
bot.send_message(110663594, 'I Am Alive Now')
bot.enable_save_next_step_handlers(
delay=2, filename="./.handler-saves/step.save")
print('Running')
bot.load_next_step_handlers()
bot.polling()
except Exception as e:
bot.send_message(110663594, "I am Dead Completely due to %s" % (e))
print(e)
pass
