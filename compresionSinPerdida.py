# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

from bitarray import bitarray

def lz77(index_front,index_back):

    #file=open('/home/alumno/Escritorio/p_manhattan.txt','r')

    #Declaracion de las ventanas
    back_buffer=[]
    front_buffer=[]
        
        
    #Crea una lista con los caracteres de la primera ventana de busqueda
    for i in range(0,index_front):
        front_buffer=file.read()
    
    #DDeclaracion bitarrays
    churro_bytes=bitarray(endian='big')
    churro_aux=bitarray(endian='big')
    
    #Iteraciones de las ventanas
    while front_buffer[index_front-1]!='':
        
    
    


    
    
    #churro_aux.frombytes(bytes(front_buffer[0], 'utf-8'))
    #churro_bytes.extend(churro_aux)
    
    
    
    #print(churro_bytes)
    
    #file.close()
    
    
    #file_compress=open('/home/alumno/Escritorio/p_manhattan_compress.txt','wb')
    #file_compress.close()
   
    
    
    
    
def find_patron(index_front,index_back,back_buffer[],front_buffer[]):
    
    posicion=[]
    
    for i in range(0,index_back):
        posicion.append(0)
    
    for i in range(0,index_back):
        if front_buffer[0]==back_buffer[i]:
            posicion[i]=1
            for j in range(i+1,(index_back)):
                if front_buffer[j-i]==back_buffer[j]:
                    posicion[i]=posicion[i]+1
                    
    largo=0
    
    for i in range(0,index_back):
        if largo<=posicion[i]:
            pos=i
                    
    return pos, largo








