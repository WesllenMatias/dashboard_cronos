from asyncio.base_events import Server
from http import server
from flask import Flask
import pymssql
import consulta


pesovendido = consulta.PesoVendido()
vendido = consulta.ValorVendido()
print(f'Peso total Vendido: {pesovendido} KG\nVenda Total: R$ {vendido}')
