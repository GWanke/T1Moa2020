#import numpy as np
from copy import deepcopy
import heapq

class Peca():
    def __init__(self,tabuleiro,pai=None,g=0):
        self.tabuleiro =tabuleiro
        self.pai=pai
        self.g = g
        self.calcH()
        self.calcF()
    #def __str__(self):
        #return "g = {} , h = {} , f = {} , pai = {},tabuleiro={}".format(self.g,self.h,self.f,self.pai,self.tabuleiro)
    def __repr__(self):
        return "{}".format(self.tabuleiro)
    def __eq__(self, other):
        return self.tabuleiro==other.tabuleiro 
    def __lt__(self,other):
        return self.f<other.f
    def __gt__(self, other):
        return self.f>other.f
    def calcH(self):
        self.h = heuristicaUm(self.tabuleiro)
    def calcF(self):
        self.f = self.g + self.h
    def __hash__(self):
        return hash(str(self.tabuleiro))
#def caminho(tabuleiro,inicio,fim):

tabuleiroFinal=[1,2,3,4,12,13,14,5,11,0,15,6,10,9,8,7]

def readInput():
    entrada = list(map(int, input().split()))
    #entrada = list(map(int, ('  12 1 3 0 11 2 15 14 10 13 8 4 9 7 6 5').split()))
    #print(entrada)  
    return entrada

def heuristicaUm(auxTab):
    count=0
    for a in range(0,16):
        if auxTab[a]!=tabuleiroFinal[a]:
            count+=1
    return  count
def geraSucessores(noPai):
    filhos=[]
    for index,it in enumerate(noPai.tabuleiro):
        if it == 0:
            indexNulo=index
    if indexNulo>=4:
        filhoCima=Peca(deepcopy(noPai.tabuleiro),noPai,noPai.g+1)
        filhoCima.tabuleiro[indexNulo], filhoCima.tabuleiro[indexNulo-4] = filhoCima.tabuleiro[indexNulo-4], 0 
        filhos.append(filhoCima)
    if indexNulo<12:
        filhoBaixo=Peca(deepcopy(noPai.tabuleiro),noPai,noPai.g+1)
        filhoBaixo.tabuleiro[indexNulo], filhoBaixo.tabuleiro[indexNulo+4] = filhoBaixo.tabuleiro[indexNulo+4], 0
        filhos.append(filhoBaixo)
    if indexNulo%4!=3:
        filhoDir=Peca(deepcopy(noPai.tabuleiro),noPai,noPai.g+1)
        filhoDir.tabuleiro[indexNulo], filhoDir.tabuleiro[indexNulo+1] = filhoDir.tabuleiro[indexNulo+1], 0 
        filhos.append(filhoDir)
    if indexNulo%4!=0:
        filhoEsq=Peca(deepcopy(noPai.tabuleiro),noPai,noPai.g+1)
        filhoEsq.tabuleiro[indexNulo], filhoEsq.tabuleiro[indexNulo-1] = filhoEsq.tabuleiro[indexNulo-1], 0
        filhos.append(filhoEsq)
    return filhos

# def dicionarioadd(dicionario,valor,key):
#     #dicionario = {k:v for k,v in zip(key,valor)}
#     dicionario[key]=valor
#     return dicionario
# def geraHash(key):
#     return hash(key)


def AEstrela(noI):
    listaAberta=[]    #heapq 
    listaFechada=[]
    heapq.heappush(listaAberta,noI)
    selecionado = listaAberta[0]
    while(len(listaAberta)!=0) and selecionado.tabuleiro!=tabuleiroFinal:
        listaFechada.append(selecionado)
        heapq.heappop(listaAberta)
        filhos = geraSucessores(selecionado)
        for filho in filhos:
            if filho in listaFechada:
                continue
            if filho in listaAberta:
                for item in listaAberta:             
                    if item==filho:
                        if filho.f>item.f or filho.f == item.f:
                            continue
            heapq.heappush(listaAberta,filho)
        selecionado=listaAberta[0]
    return selecionado.g


def main():
    inicial = Peca(readInput())
    resultado=AEstrela(inicial)
    print(resultado)
if __name__ == '__main__':
    main()
