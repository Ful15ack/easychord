'''
Created on 18 jul. 2019

@author: sebas
'''
from io import open

archivoAuxiliar="auxca.acec"

# ************ ESCRIBIR Y CREAR SI NO EXISTE UN ARCHIVO TXT ******************
def escribirCrearArchivo(archivoEscribir):
    try:
        archivoExterno=open(archivoAuxiliar, "w")
        archivoExterno.writelines(archivoEscribir)
        archivoExterno.close()
    except:
        print('error escribirCrearArchivo')
    
    
# ************* LEER LINEAS Y GUARDARLO EN UNA LISTA CADA RENGLoN  ****************
def abrirCancionSeleccionada(abrirArchivo):
    try:
        archivoExterno=open(abrirArchivo, "r")
        archivoPrincipal=archivoExterno.readlines()
        escribirCrearArchivo(archivoPrincipal)
        archivoExterno.close()
        
        return archivoPrincipal
    except:
        print('error abrirCancionSeleccionada')

# ************* LEER LINEAS Y GUARDARLO EN UNA LISTA CADA RENGLoN  ****************
def abrirAuxiliar():
    archivoExterno=open("auxca.acec", "r")
    auxiliar=archivoExterno.readlines()
    archivoExterno.close()
    
    return auxiliar

#**************** TRANSPORTA LAS NOTAS MEDIO TONO HACIA ARRIBA ********************
def transportarMedioArriba(listaX):

    nuevaLista=[]
    listaAux=[]
    lineaAux=''
    
    for linea in listaX:
        ultima=''   
        if linea[0]=='.':
            listaAux.append('.')
            for char in linea:                
                if char!='#' and ultima=='A':
                    listaAux.append('Bb')
                if (char=='b' and ultima=='B') or (char=='#' and ultima=='A'):
                    listaAux.append('B')
                if char!='b' and ultima=='B':
                    listaAux.append('C')
                if char!='#' and ultima=='C':
                    listaAux.append('C#')
                if char=='#' and ultima=='C' or (char=='b' and ultima=='D'):
                    listaAux.append('D')
                if char!='#' and ultima=='D':
                    listaAux.append('Eb')
                if (char=='b' and ultima=='E') or (char=='#' and ultima=='D'):
                    listaAux.append('E')
                if char!='b' and ultima=='E':
                    listaAux.append('F')
                if char!='#' and ultima=='F':
                    listaAux.append('F#')
                if char=='#' and ultima=='F' or (char=='b' and ultima=='G'):
                    listaAux.append('G')
                if char!='#' and ultima=='G':
                    listaAux.append('G#')
                if char=='#' and ultima=='G' or (char=='b' and ultima=='A'):
                    listaAux.append('A')
                if char!='A' and char!='B' and char!='C' and char!='D' and char!='E' and char!='F' and char!='G' and char!='#' and char!='b' and char!='.' and char!='\n':
                    listaAux.append(char)
    
                ultima=char 
                           
            listaAux.append('\n')        
            lineaAux=lineaAux.join(listaAux)
            nuevaLista.append(lineaAux)
            lineaAux=''
            del listaAux[:]
            
        if linea[0]!='.':
            if linea[0]!=' ':
                nuevaLista.append(' '+linea)
            if linea[0]==' ':         
                nuevaLista.append(linea)
    escribirCrearArchivo(nuevaLista)        
    return nuevaLista

#**************** TRANSPORTA LAS NOTAS MEDIO TONO HACIA ARRIBA ********************
def transportarMedioAbajo(listaX):

    nuevaLista=[]
    listaAux=[]
    lineaAux=''
    
    for linea in listaX:
        ultima=''   
        if linea[0]=='.':
            listaAux.append('.')
            for char in linea:                
                if char!='#' and ultima=='A':
                    listaAux.append('G#')
                if (char=='b' and ultima=='B') or (char=='#' and ultima=='A'):
                    listaAux.append('A')
                if char!='b' and ultima=='B':
                    listaAux.append('Bb')
                if char!='#' and ultima=='C':
                    listaAux.append('B')
                if char=='#' and ultima=='C' or (char=='b' and ultima=='D'):
                    listaAux.append('C')
                if char!='#' and ultima=='D':
                    listaAux.append('C#')
                if (char=='b' and ultima=='E') or (char=='#' and ultima=='D'):
                    listaAux.append('D')
                if char!='b' and ultima=='E':
                    listaAux.append('Eb')
                if char!='#' and ultima=='F':
                    listaAux.append('E')
                if char=='#' and ultima=='F' or (char=='b' and ultima=='G'):
                    listaAux.append('F')
                if char!='#' and ultima=='G':
                    listaAux.append('F#')
                if char=='#' and ultima=='G' or (char=='b' and ultima=='A'):
                    listaAux.append('G')
                if char!='A' and char!='B' and char!='C' and char!='D' and char!='E' and char!='F' and char!='G' and char!='#' and char!='b' and char!='.' and char!='\n':
                    listaAux.append(char)
    
                ultima=char 
                           
            listaAux.append('\n')        
            lineaAux=lineaAux.join(listaAux)
            nuevaLista.append(lineaAux)
            lineaAux=''
            del listaAux[:]
            
        if linea[0]!='.':
            if linea[0]!=' ':
                nuevaLista.append(' '+linea)
            if linea[0]==' ':         
                nuevaLista.append(linea)
    escribirCrearArchivo(nuevaLista)        
    return nuevaLista
