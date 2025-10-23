from fastapi import FastApi
import sqlite3
from models import Vehiculo, Destino
from database import crear_tablas


crear_tablas()

app = FastApi(title="transportes Sigmotoa")