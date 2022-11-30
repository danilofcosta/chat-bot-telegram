#pip install pytelegramapibot
#pip install  wikipedia

from tokem import tokem as chavet
from defs import*
import telebot,random,json,os
import logging

bot = telebot.TeleBot(chavet)
temp=[]
memory=load()
def verificar(mensagem):
    if mensagem.chat.first_name ==' Nome':
        nameid=mensagem.chat.title
    else:
        nameid=mensagem.chat.first_name  
        if mensagem.chat.id not in memory['invazao_de_pv'] and mensagem.chat.type =="private":
            database_joson(nameid,mensagem.from_user.id ,'invazao_de_pv')
        print(mensagem.text)
    return True


@bot.message_handler(commands=["start"])
def start(mensagem):
    bot.send_message(mensagem.chat.id,f'{mensagem.chat.first_name} Dizem que não e bom invadir pv sem pedir mais enfim......\n tudo bem?')

@bot.message_handler(commands=["wikipedia"])
def swiki(mensagem):
    #print('iniciando pesquisa '+ mensagem.text[10:])
    try:
        import wikipedia
        wikipedia.set_lang("pt")
        busca=mensagem.text[10:]
        resultado=wikipedia.summary(busca)
        fbusca=f'''
        {busca}\n
        {resultado}
        
        '''
        resultado=wikipedia.summary(busca)
        bot.send_message(mensagem.chat.id,fbusca)
    except:
        bot.send_message(mensagem.chat.id,f'Eu não consegui fazer a busca de {busca} ') 


@bot.message_handler (content_types=["sticker"]) #pronto 
def sticker (mensagem):
    memory=load() 
    nick=f'{mensagem.sticker.set_name}={mensagem.sticker.file_unique_id}-{mensagem.sticker.emoji}'
    #bot.send_sticker(mensagem.chat.id,memory['sticker'][nick])
    s=0
    if  nick in memory['sticker']:
        ran=random.randint(1,len(memory['sticker']))
        for k in memory['sticker'].keys():

            if s != ran:
                s+=1
            elif s == ran:
                rsticker=k
                break
        try:
            bot.send_sticker(mensagem.chat.id,memory['sticker'][rsticker])
        except(UnboundLocalError):
            bot.send_message(mensagem,"OU OU OU Sem flood !")
            
    else:            
        database_joson(nick,mensagem.sticker.file_id,'sticker')
        



@bot.message_handler(func=verificar)
def responder(mensagem):
    msguser=mensagem.text
    memory=load()
    memory=memory['messagem_txt']
    if  'qual é meu nome?'in msguser.lower() :
        bot.reply_to(mensagem,f' Seu nome {mensagem.chat.first_name}')
        bot.send_message(mensagem.chat.id,'esqueceu?')
    elif msguser in memory:
        bot.reply_to(mensagem,memory[mensagem.text])
    else:
        if len(temp) == 0:
            temp.append(msguser)
        else:
            autosave=msguser
            database_joson(temp[0],autosave)
            #bot.send_message(mensagem.chat.id,f'da proxima vez irei responder isso \n {temp[0],autosave}')
            temp.clear()

def create_database (nome_aquivo='database'):
    import os,json
    #criada aquivo .json
    loading=os.getcwd()
    start={'messagem_txt':{'oi':'ola'},"invazao_de_pv": {'NOME':'id'},"sticker":{"id unico":'file id'}}
    for file in os.listdir(loading):
        if file == f'{nome_aquivo}.json':
            return f'{nome_aquivo}.json'
        #verifica se a um aquivo com o nome caso nao cria com uma base da variavel start
    a=open(nome_aquivo+'.json','w')
    a.close()
    with open(f'{nome_aquivo}.json','w') as lfile:
        json.dump(start,lfile)
        print(f'aquivo {nome_aquivo}.json foi criado') 
        return f'{nome_aquivo}.json'
     

def database_joson(chave='',valor=0,namekye='messagem_txt',database='database'):
    import json
    #criada aquivo .json
    with open(f'{database}.json','r') as  databaseLoad:
        aquivoload=json.load(databaseLoad)#carrega o que esta salvo na base de dados ecoloca em uma variavel /dicionario         
        aquivoload[namekye][chave]=valor
        with open(f'{database}.json','w') as  databasesave:
            json.dump(aquivoload,databasesave,indent=4)

def load ():
    a=create_database('database')

    with open(a,'r') as file:
        login=json.load(file)
    return login

#vericação de updates continua
 
bot.polling(non_stop=True)
bot.send_message(chatid dono bot,eu tive um err 54541o ')
