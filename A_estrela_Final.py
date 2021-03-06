
import heapq
import time
tabuleiroFinal=(1,2,3,4,12,13,14,5,11,0,15,6,10,9,8,7)

dict_pos = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (0, 3),
    12: (1, 0),
    13: (1, 1),
    14: (1, 2),
    5: (1, 3),
    11: (2, 0),
    0: (2, 1),
    15: (2, 2),
    6: (2, 3),
    10: (3, 0),
    9: (3, 1),
    8: (3, 2),
    7: (3, 3),
} 
    
class Peca():
    def __init__(self, tabuleiro, indexZero, pai = None, g = 0):
        self.tabuleiro = tabuleiro
        self.indexZero=indexZero
        self.pai = pai
        self.g = g
        self.f = g + heuristicaTres(tabuleiro)
    def __repr__(self):
        return "{}".format(self.tabuleiro)
    def __eq__(self, other):
        return self.tabuleiro == other.tabuleiro 
    def __lt__(self,other):
        return self.f < other.f
    def __hash__(self):
        return hash(self.tabuleiro)

def readInput():
    entrada=tuple(map(int, input().split()))
    #entrada = list(map(int, ('  12 1 3 0 11 2 15 14 10 13 8 4 9 7 6 5').split()))
    return entrada,get_indexInicio(entrada)

def heuristicaUm(tabuleiro):
    count=0
    for a in range(0,16):
        if tabuleiro[a]!=tabuleiroFinal[a]:
            count+=1
    #return len(list(filter(lambda x: x[0] != x[1], zip(tabuleiro, tabuleiroFinal))))
    return count


def Spiral(matriz):
    #print (type(matriz))
    #RECURSIVIDADE. -> Tira a primeira linha da matriz, rotaciona a matriz, adiciona a primeira linha.
    #Ex: [0 1 2 3] , [4,5,6,7] , [8,9,10,11].[12,13,14,15] = [0,1,2,3] + Spiral[[7,11,15],[6,10,14],[5,9,13],[4,8,12]] = ...
    #return matriz and list(matriz.pop(0)) + Spiral(zip(*matriz)[::-1])      #->Python 2
    return matriz and [*matriz.pop(0)] + Spiral([*zip(*matriz)][::-1])     #->Python 3

def heuristicaDois(tabuleiro):
    caracol=list(range(0,16))
    count=0
    aux=0
    mat=[]
    #transforma em matriz
    for i in range(4):
        mat.append([]) 
        for j in range(4):
            mat[i].append(tabuleiro[aux])
            aux+=1 
    #transforma em caracol        
    caracol=Spiral(mat)
    #calcula a heuristica  
    for ind,item in enumerate(caracol):
        if ind > 0 and ind < 14:
            if caracol[ind +1] != item + 1:
                count += 1
    return count



def heuristicaTres(tabuleiro):
    ManhattamDist = 0
    for i,item in enumerate(tabuleiro):
        xAtual,yAtual = int(i/ 4) , i % 4
        xObjetivo,yObjetivo = dict_pos[item][0],dict_pos[item][1]
        ManhattamDist += abs(xAtual - xObjetivo) + abs(yAtual - yObjetivo)
    return ManhattamDist

def heuristicaQuatro(tabuleiro):
    h1=heuristicaUm(tabuleiro)
    h2=heuristicaDois(tabuleiro)
    h3=heuristicaTres(tabuleiro)
    return int(0.15 * (h1) + 0.05 *(h2) + 0.8 * (h3))

def heuristicaCinco(tabuleiro):
    return max(heuristicaUm(tabuleiro),heuristicaDois(tabuleiro),heuristicaTres(tabuleiro))


def get_indexInicio(tabuleiro):
    for index,item in enumerate(tabuleiro):
        if item == 0:
            indexNulo=index
            return indexNulo

def swap_tuple(set_to_swap, index_origin, index_dest):
    to_list = list(set_to_swap)
    to_list[index_dest], to_list[index_origin] = to_list[index_origin], to_list[index_dest]
    return tuple(to_list)

def geraSucessores(noPai):
    if noPai.indexZero >= 4:
        newIndexNulo = noPai.indexZero - 4
        yield swap_tuple(noPai.tabuleiro, noPai.indexZero, newIndexNulo), newIndexNulo

    if noPai.indexZero <12 :
        newIndexNulo = noPai.indexZero + 4
        yield swap_tuple(noPai.tabuleiro, noPai.indexZero, newIndexNulo), newIndexNulo

    if noPai.indexZero %4 != 3:
        newIndexNulo = noPai.indexZero + 1
        yield swap_tuple(noPai.tabuleiro, noPai.indexZero, newIndexNulo), newIndexNulo

    if noPai.indexZero %4 != 0:
        newIndexNulo = noPai.indexZero - 1
        yield swap_tuple(noPai.tabuleiro, noPai.indexZero, newIndexNulo), newIndexNulo


def AEstrela(noI):
    start = time.process_time()
    listaAberta = []        #heapq 
    listaFechada = set()   #set
    heapq.heappush(listaAberta, noI)
    selecionado = heapq.heappop(listaAberta)
    while selecionado.tabuleiro != tabuleiroFinal:
        listaFechada.add(selecionado.tabuleiro)
        for filho, indexZero in geraSucessores(selecionado):
            if filho not in listaFechada:
                heapq.heappush(listaAberta, Peca(filho, indexZero, selecionado, selecionado.g + 1))
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
