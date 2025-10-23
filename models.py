from pydantic import BaseModel

class Vehiculo(BaseModel):
    placa: str
    marca: str
    capacidad: int
    modelo: int

class Destino(BaseModel):
    destino: str
    distancia: float
    tiempo: str
    id_vehiculo: int

    