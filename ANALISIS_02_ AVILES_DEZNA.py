#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 20:05:18 2021

@author: Ilusionista
"""

import csv 

totales = []

with open ("synergy.csv", "r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    #exportaciones en total
   
    for linea in lector:
        if linea[9] == "total_value":
            continue
        
        totales.append(int(linea[9]))
        
        
print("El total de las exportaciones e importaciones entre 2015 y 2020 de la empresa Synergy es:  ",sum(totales))




#exportaciones por pais
#DICCIONARIOS
exp_mexico = []

with open ("synergy.csv", "r") as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    
    for linea in lector:
        if linea["origin"] == "Mexico":
            exp_mexico.append(int(linea["total_value"]))
            
print(exp_mexico)
print ("Exportaciones totales de Mexico:  ", sum(exp_mexico))



#total de exportaciones 
exp_total = []

with open ("synergy.csv", "r") as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    
    for linea in lector:
        if linea["direction"] == "Exports":
            exp_total.append(int(linea["total_value"]))
            
print(exp_total)
print ("Exportaciones totales de Synergy:  ", sum(exp_total))



#tipo de transporte

mexico_transporte = []

with open ("synergy.csv", "r") as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    
    for linea in lector:
        if linea["origin"] == "Mexico":
            mexico_transporte.append(linea["transport_mode"])
            
print("Los nomdos de transporte que usa mexico son:   ", (mexico_transporte))

numero_operaciones = len(mexico_transporte)
print(numero_operaciones)




#repeticiones en exportaciones de Mexico 

mexico_transporte = []
with open ("synergy.csv", "r") as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    
    for linea in lector:
        if linea["origin"] == "Mexico":
            mexico_transporte.append(linea["transport_mode"])
            

numero_operaciones = len(mexico_transporte)

sea = mexico_transporte.count("Sea")
print("Se realizaron:   ",(sea))

Rail = mexico_transporte.count("Rail")
print("Se realizaron transacciones en tren:   ",(Rail))

Road = mexico_transporte.count("Road")
print("Se realizaron transacciones terrestres:   ",(Road))





    
  
    