from fastapi import FastAPI

APP = FastAPI()

@APP.get('/')

def raiz():
    return {'Mensagem':'API da Biblioteca no Ar!'}

@APP.get('/Livros')
def livros():
    return {'Mensagem':'Lista de livros disponiveis.'} 
