from grafos import mapas
import pdb
from functions import get_grau
from functions import get_vertices_do_grau
from functions import where

mapa = {
    'BSB':[('TAG',1),('AP',3),('GO',4)],
    'TAG':[('BSB',1)],
    'AP':[('BSB',3), ('JP',9),('CER',5)],
    'CER':[('AP',5),('JP',8),('GO',3)],
    'GO':[('BSB',4),('CER', 3)],
    'JP':[('AP',9),('CER',4)] 
}

print(mapas["adjacency_matrix"])
ll = mapas["adjacency_listNW"]

print (where(ll,'BSB'))
