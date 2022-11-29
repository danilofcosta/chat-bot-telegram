#pip install pytelegramapibot
from tokem import tokem as chavet
from defs import*
import telebot,random


bot = telebot.TeleBot(chavet)
temp=[]
try:
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
            bot.send_message(mensagem.chat.id,f'eu não consegui fazer a busca de{busca} ') 


    @bot.message_handler (content_types=["sticker"]) 
    def sticker (mensagem):
        memory=load() 
        print('eu recebi stiker',ran)
        nick=f'{mensagem.sticker.set_name}={mensagem.sticker.file_unique_id}-{mensagem.sticker.emoji}'
        #bot.send_sticker(mensagem.chat.id,memory['sticker'][nick])
        if  nick in memory['sticker']:
            ran=random.randint(1,len(memory['sticker']))
            s=0
            for k,v in memory['sticker'].items:
                if s != ran:
                    s+=1
                else:
                    
            print('eu enareei stiker') 
            bot.send_sticker(mensagem.chat.id,memory['sticker'][nick])
        else:
            print('SALVEI')
            
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
            #print(f'resposta{(memory[mensagem.text])}')
            bot.reply_to(mensagem,memory[mensagem.text])
        else:
            if len(temp) == 0:
                temp.append(msguser)
                #print(temp)
                #bot.reply_to(mensagem,f'o que devo responder da proxima vez que me mandarem \n > {temp[0]} <')
            else:
                autosave=msguser
                database_joson(temp[0],autosave)
                #bot.send_message(mensagem.chat.id,f'da proxima vez irei responder isso \n {temp[0],autosave}')
                temp.clear()
                #print(temp)
    #vericação de updates continua
    

except:
    bot.send_message('eu tive um erro ')
bot.polling(none_stop=False)
