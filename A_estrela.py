#import numpy as np
from copy import deepcopy
import heapq
import time

tabuleiroFinal=[1,2,3,4,12,13,14,5,11,0,15,6,10,9,8,7]

class Peca():
    def __init__(self, tabuleiro, pai = None, g = 0):
        self.tabuleiro = tabuleiro
        self.pai = pai
        self.g = g
        self.f = g + heuristicaUm(tabuleiro)
    #def __str__(self):
        #return "g = {} , h = {} , f = {} , pai = {},tabuleiro={}".format(self.g,self.h,self.f,self.pai,self.tabuleiro)
    def __repr__(self):
        return "{}".format(self.tabuleiro)
    def __eq__(self, other):
        return self.tabuleiro == other.tabuleiro 
    def __lt__(self,other):
        return self.f < other.f
    def __gt__(self, other):
        return self.f > other.f
    def __hash__(self):
        return hash(str(self.tabuleiro))
#def caminho(tabuleiro,inicio,fim):
def readInput():
    #entrada = list(map(int, input().split()))
    entrada = list(map(int, ('  12 1 3 0 11 2 15 14 10 13 8 4 9 7 6 5').split()))  
    return entrada

def heuristicaUm(auxTab):
    count=0
    for a in range(0,16):
        if auxTab[a]!=tabuleiroFinal[a]:
            count+=1
    return count

def geraSucessores(noPai):
    filhos=[]
    for index,it in enumerate(noPai.tabuleiro):
        if it == 0:
            indexNulo=index
    if indexNulo >= 4:
        filhoCima=Peca(noPai.tabuleiro[:],noPai,noPai.g + 1)
        filhoCima.tabuleiro[indexNulo], filhoCima.tabuleiro[indexNulo - 4] = filhoCima.tabuleiro[indexNulo - 4], 0 
        yield filhoCima
    if indexNulo <12 :
        filhoBaixo=Peca(noPai.tabuleiro[:],noPai,noPai.g + 1)
        filhoBaixo.tabuleiro[indexNulo], filhoBaixo.tabuleiro[indexNulo + 4] = filhoBaixo.tabuleiro[indexNulo + 4], 0
        yield filhoBaixo
    if indexNulo %4 != 3:
        filhoDir=Peca(noPai.tabuleiro[:],noPai,noPai.g+1)
        filhoDir.tabuleiro[indexNulo], filhoDir.tabuleiro[indexNulo+1] = filhoDir.tabuleiro[indexNulo+1], 0 
        yield filhoDir
    if indexNulo %4 != 0:
        filhoEsq=Peca(noPai.tabuleiro[:],noPai,noPai.g+1)
        filhoEsq.tabuleiro[indexNulo], filhoEsq.tabuleiro[indexNulo-1] = filhoEsq.tabuleiro[indexNulo-1], 0
        yield filhoEsq


def AEstrela(noI):
    start=time.process_time()
    listaAberta=[]        #heapq 
    listaFechada=set()   #set
    heapq.heappush(listaAberta,noI)
    while(selecionado := heapq.heappop(listaAberta)) and selecionado.tabuleiro!= tabuleiroFinal:
        listaFechada.add(selecionado)
        [heapq.heappush(listaAberta,filho) for filho in geraSucessores(selecionado) if filho not in listaFechada]                        
    print(time.process_time() - start)
    return selecionado.g


def main():
    inicial = Peca(readInput())
    resultado=AEstrela(inicial)
    print(resultado)
if __name__ == '__main__':
    main()
