from tokem import tokem as chavet
from defs import*
import telebot,os
bot = telebot.TeleBot(chavet)
temp=[]
memory=load()

#verifica se chegou mensagem
def verificar(mensagem):
    if mensagem.chat.id not in memory['Conhecidos']:
        database_joson(mensagem.chat.first_name,mensagem.chat.id,'Conhecidos')
    print(mensagem.text)
  
    return True
@bot.message_handler(commands=["start"])
def start(mensagem):
    bot.send_message(mensagem.chat.id,f'{mensagem.chat.first_name} Dizem que não e bom invadir pv sem pedir mais enfim......\n tudo bem?')

@bot.message_handler(func=verificar)
def responder(mensagem):
    msguser=mensagem.text
    memory=load()
    memory=memory['messafem_txt']

    if  'qual meu nome?'in msguser.lower() :
        bot.reply_to(mensagem,f' Seu nome {mensagem.chat.first_name}')
        bot.send_message(mensagem.chat.id,'esqueceu?')


    elif msguser in memory:
        bot.reply_to(mensagem,memory[mensagem.text])
    else:
        if len(temp) == 0:
            temp.append(msguser)
            print(temp)
            bot.reply_to(mensagem,f'o que devo responder da proxima vez que me mandarem \n > {temp[0]} <')
        else:
            autosave=msguser
            database_joson(temp[0],autosave)
            bot.send_message(mensagem.chat.id,f'da proxima vez irei responder isso \n {temp[0],autosave}')
            temp.clear()
            print(temp)
#vericação de updates continua
bot.polling()
