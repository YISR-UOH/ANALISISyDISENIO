
from flask import render_template
import requests
from bs4 import BeautifulSoup

def datos(url):
    url=url.replace("FormEgreso","FormEgresoF02",1)
    req = requests.get(url)

    soup = BeautifulSoup(req.text,"html.parser")
    lista=['lblRazonSocial','lblRutEmp','lblNombreRL','lblRutRL','lblDomL','lblOrgAdm16744','lblFechaOrigen','lblFunc']
    lista2 = ['lblRegion','lblIct','lblAgno','lblFisc']
    lista3=['lblTotal','lblTotalExt','lblTotalMen']
    datos={}
    info={}
    trabajadores={}
    for i in lista:
        a=(soup.find_all(id=i))
        datos[i]=list(a[0])
    for i in lista2:
        a=(soup.find_all(id=i))
        info[i]=list(a[0])
    for i in lista3:
        a=(soup.find_all(id=i))
        trabajadores[i]=list(a[0])
    return [datos,info,trabajadores]