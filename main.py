#Importando FastAPI epara o projeto 
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

#Instanciando o FastAPI em variavel
app = FastAPI()

class VeiculoModel(BaseModel):
    id: int
    nome: str
    pessoas: int

frota = [
    {
        "id": 1,
        "nome": "Fox",
        "pessoas": 5
    },
     {
        "id": 2,
        "nome": "Logan",
        "pessoas": 5
    },
     {
        "id": 3,
        "nome": "Golf",
        "pessoas": 5
    },
     {
        "id": 4,
        "nome": "Onibus",
        "pessoas": 10
    } ,   
]

#Obtendo info todos os carros
@app.get("/frota")
def obter_frota():
    return frota

#Obtendo info carro especifico 
@app.get("/frota/{id}")
async def obtendo_carros(id: int):
    for item in frota:
        if item["id"] == id:
            return item
    return {"error": "Item não encontrado"}

#Criar info carro novo
@app.post("/frota/novo")
async def adicionar_veiculo(item: VeiculoModel):
    frota.append(item)
    return {"Sucesso": "Item cadastrado"}

#Atualizar info carro
@app.put("/frota/mudando/{id}")
async def atualizar_itm(id: int, item: VeiculoModel):
    for i, existing_item in enumerate(frota):
        if existing_item["id"] == id:
            frota[i] = item.dict()
            return {"message": "Item atualizado com sucesso"}        

#Deletando um Carro
@app.delete("/frota/deletando/{id}")
async def deeletando_carro(id: int):
    for i, existing_item in enumerate(frota):
        if existing_item["id"] == id:
            del frota[i]
    return {"Item excluido com sucesso"}














if __name__ == "__main__":
    uvicorn.run(app, port=8000)
