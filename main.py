from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


APP = FastAPI()

class livro(BaseModel):
    id: int
    titulo: str
    autor: bool = True


@APP.get('/')

def raiz():
    return {'Mensagem':'API da Biblioteca no Ar!'}

@APP.get('/livros')
def livros():
    return {'Mensagem':'Lista de livros disponiveis.'} 


@APP.get('/livros/{id}')
def livros_id(id: int):
    return {'Mensagem':f'Livro com id {id}.'}

@APP.get('/autores/')
def autores():
    return {'Mensagem':'Lista de autores disponiveis.'}

@APP.get('/autores/{id}')
def autores_id(id:int):
    return {'Mensagem':f'Autor com id {id}.'}

class livro:
    def __init__(self, id:int, titulo:str, autor:str):
        self.id = id
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f'livro(id={self.id}, titulo={self.titulo}, autor={self.autor})'
    
def get_livro_by_id(id:int):

    for  i in range(1,10):
        if i == id:
            livro = livro(id=i, titulo=f'Titulo {i}', autor=f'Autor {i}')
            return livro
        raise HTTPException(status_code=404, detail=f'livro com id {id} não encontrado')

#---------------POST-----------------#

def post_livro(livro: livro):
    novo= livro.model_dump()
    novo['id'] = max([livro.id for livro in livros], default=0) + 1
    livros.append(novo)
    return {'Mensagem': f'livro com id {livro.id} adicionado com sucesso.'}

#----------------PUT-----------------#

def atualizar_livro(id:int, livro: livro):
    for i, l in enumerate(livros):
        if l.id == id:
            livros[i] = livro
            return {'Mensagem': f'livro com id {id} atualizado com sucesso.'}
    raise HTTPException(status_code=404, detail=f'livro com id {id} não encontrado')