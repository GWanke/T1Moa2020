#import numpy as np
from copy import deepcopy

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
        return hash(repr(self))
#def caminho(tabuleiro,inicio,fim):

tabuleiroFinal=[1,2,3,4,12,13,14,5,11,0,15,6,10,9,8,7]

def readInput():
    entrada = list(map(int, input().split()))
    #listaEntrada=str(input()).split(' ')
    #entrada=[]
    #for i in range(0,16):
        #entrada.append(int(listaEntrada[i]))
    #print(entrada)
    #listaEntrada=str("1 3 4 5 12 2 14 6 11 13 15 7 0 10 9 8").split()
    #entrada = list(map(int,listaEntrada))
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

def AEstrela(noI):
    listaAberta=[]    #pqueue 
    listaFechada=[]     ##definir dps. ->>>map????????
    listaAberta.append(noI)
    selecionado=min(listaAberta)
    count=0
    while(len(listaAberta)!=0) and selecionado.tabuleiro!=tabuleiroFinal:# and count<=10:
        count+=1
        listaFechada.append(selecionado)
        for ind,item in enumerate(listaAberta):
            if item==selecionado:
                indsel=ind
        listaAberta.pop(indsel)
        filhos = geraSucessores(selecionado)
        for filho in filhos:
            if filho in listaFechada:
                continue
            for noA in listaAberta:
                if filho.tabuleiro==noA.tabuleiro:
                    if filho.f>noA.f or filho.f ==noA.f:
                        #print("k")
                        continue
            listaAberta.append(filho)
        selecionado=min(listaAberta)
    print(selecionado.g)
    valor=map(hash,listaAberta)
    teste = {k:v for k,v in zip(listaAberta,valor)}
    print(teste)

def main():
    inicial = Peca(readInput())
    AEstrela(inicial)
if __name__ == '__main__':
    main()
