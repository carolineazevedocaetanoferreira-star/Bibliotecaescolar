from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


APP = FastAPI()

#-------livro-----#
class Livro(BaseModel):
    id: int
    titulo: str
    autor: str


    #-----Banco de dados-----#
livros = [
    Livro(id=1, titulo="Dom Casmurro", autor="Machado de Assis"),
    Livro(id=2, titulo="O Pequeno Príncipe", autor="Antoine de Saint-Exupéry"),
]


# ------------------- RAIZ -----------------
@APP.get("/livros")
def listar_livros():
    return {'Mensagem':'API da Biblioteca no Ar!'}


@APP.get("/livros/{id}")
def buscar_livro(id: int):
    for livro in livros:
        if livro.id == id:
            return livro

        raise HTTPException(
        status_code=404,
        detail=f"Livro com id {id} não encontrado."
    )

#------------------- AUTORES -------------------#


@APP.get("/autores")
def listar_autores():
    return [livro.autor for livro in livros]

@APP.get("/autores/{id}")
def buscar_autor(id: int):
    for livro in livros:
        if livro.id == id:
            return {"autor": livro.autor}

    raise HTTPException(
        status_code=404,
        detail=f"Autor do livro {id} não encontrado."
    )



#---------------POST-----------------#


@APP.post("/livros")
def post_livro(livro: Livro):
    livros.append(livro)

    return {
        'Mensagem': f'Livro com id {livro.id} adicionado com sucesso.'
    }

#----------------PUT-----------------#


@APP.put("/livros/{id}")
def atualizar_livro(id: int, livro: Livro):
    for i, l in enumerate(livros):
        if l.id == id:
            livros[i] = livro

            return {'Mensagem': f'Livro com id {id} atualizado com sucesso.'}

    raise HTTPException(status_code=404,
        detail=f'Livro com id {id} não encontrado')


#----------------DELETE-----------------#

@APP.delete("/livros/{id}")
def deletar_livro(id: int):
    for i, l in enumerate(livros):
        if l.id == id:
            del livros[i]

            return {'Mensagem': f'Livro com id {id} removido com sucesso.'}

    raise HTTPException(status_code=404,
        detail=f'Livro com id {id} não encontrado')
