
import heapq
import time
tabuleiroFinal=[1,2,3,4,12,13,14,5,11,0,15,6,10,9,8,7]
    
class Peca():
    def __init__(self, tabuleiro, indexZero, pai = None, g=0):
        self.tabuleiro = tabuleiro
        self.indexZero=indexZero
        self.pai = pai
        self.g = g
        self.f = g + heuristicaUm(tabuleiro)
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

def readInput():
    entrada=list(map(int, input().split()))
    return entrada,get_indexInicio(entrada)

def heuristicaUm(tabuleiro):
    count=0
    for a in range(0,16):
        if tabuleiro[a]!=tabuleiroFinal[a]:
            count+=1
    #return len(list(filter(lambda x: x[0] != x[1], zip(tabuleiro, tabuleiroFinal))))
    return count
def get_indexInicio(tabuleiro):
    for index,item in enumerate(tabuleiro):
        if item == 0:
            indexNulo=index
            return indexNulo

def geraSucessores(noPai):
    if noPai.indexZero >= 4:
        filhoCima=Peca(noPai.tabuleiro[:], 0,noPai,noPai.g + 1)
        filhoCima.indexZero = noPai.indexZero - 4
        filhoCima.tabuleiro[noPai.indexZero], filhoCima.tabuleiro[noPai.indexZero - 4] = filhoCima.tabuleiro[noPai.indexZero - 4], 0 
        yield filhoCima
    if noPai.indexZero <12 :
        filhoBaixo=Peca(noPai.tabuleiro[:],0,noPai,noPai.g + 1)
        filhoBaixo.indexZero = noPai.indexZero + 4
        filhoBaixo.tabuleiro[noPai.indexZero], filhoBaixo.tabuleiro[noPai.indexZero + 4] = filhoBaixo.tabuleiro[noPai.indexZero + 4], 0
        yield filhoBaixo
    if noPai.indexZero %4 != 3:
        filhoDir=Peca(noPai.tabuleiro[:],0,noPai,noPai.g + 1)
        filhoDir.indexZero = noPai.indexZero + 1
        filhoDir.tabuleiro[noPai.indexZero], filhoDir.tabuleiro[noPai.indexZero + 1] = filhoDir.tabuleiro[noPai.indexZero +1 ], 0 
        yield filhoDir
    if noPai.indexZero %4 != 0:
        filhoEsq=Peca(noPai.tabuleiro[:],0,noPai,noPai.g+1)
        filhoEsq.indexZero = noPai.indexZero - 1
        filhoEsq.tabuleiro[noPai.indexZero], filhoEsq.tabuleiro[noPai.indexZero - 1] = filhoEsq.tabuleiro[noPai.indexZero - 1], 0
        yield filhoEsq


def AEstrela(noI):
    start=time.process_time()
    listaAberta=[]        #heapq 
    listaFechada=set()   #set
    heapq.heappush(listaAberta,noI)
    selecionado = heapq.heappop(listaAberta)
    while(len(listaAberta)>-1) and selecionado.tabuleiro!= tabuleiroFinal:
        listaFechada.add(selecionado)
        [heapq.heappush(listaAberta,filho) for filho in geraSucessores(selecionado) if filho not in listaFechada]
        selecionado = heapq.heappop(listaAberta)                        
    print(time.process_time() - start)
    return selecionado.g


def main():
    inicial,ind0 = readInput()
    pecaInicio = Peca(inicial,ind0)
    resultado = AEstrela(pecaInicio)
    print(resultado)
if __name__ == '__main__':
    main()
