import json,os
def create_database (nome_aquivo):
    import os,json
    #criada aquivo .json
    loading=os.getcwd()
    start={'oi':'ola'}
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
     

def database_joson(chave,valor,database='database'):
    import json
    #criada aquivo .json
    with open(f'{database}.json','r') as  databaseLoad:
        aquivoload=json.load(databaseLoad)#carrega o que esta salvo na base de dados ecoloca em uma variavel /dicionario
        aquivoload[chave]=valor
        with open(f'{database}.json','w') as  databasesave:
            json.dump(aquivoload,databasesave,indent=4)

def load ():
    a=create_database('database')
    print(a)
    with open(a,'r') as file:
        dir=json.load(file)
    return dir


def chat():
    os.system('cls')
    dir=load()
    chat=input('diga algo=>')
    while True:
        if chat in dir :
            print(dir[chat])
        else:
            autosave=input(f'o que devo responder a "{chat}" ??')
            dir[chat]=autosave.title()
            database_joson(dir[chat],autosave)
        chat=input('=>')
        if chat =='sair':
            break

