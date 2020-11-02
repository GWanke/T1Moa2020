#!/bin/env python3
import heapq
import time
import psutil
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

h3memo = [[0 for x in range(16)] for y in range(16)] 

h3memo[1][0] = 0
h3memo[1][1] = 1
h3memo[1][2] = 2
h3memo[1][3] = 3
h3memo[1][4] = 1
h3memo[1][5] = 2
h3memo[1][6] = 3
h3memo[1][7] = 4
h3memo[1][8] = 2
h3memo[1][9] = 3
h3memo[1][10] = 4
h3memo[1][11] = 5
h3memo[1][12] = 3
h3memo[1][13] = 4
h3memo[1][14] = 5
h3memo[1][15] = 6
h3memo[2][0] = 1
h3memo[2][1] = 0
h3memo[2][2] = 1
h3memo[2][3] = 2
h3memo[2][4] = 2
h3memo[2][5] = 1
h3memo[2][6] = 2
h3memo[2][7] = 3
h3memo[2][8] = 3
h3memo[2][9] = 2
h3memo[2][10] = 3
h3memo[2][11] = 4
h3memo[2][12] = 4
h3memo[2][13] = 3
h3memo[2][14] = 4
h3memo[2][15] = 5
h3memo[3][0] = 2
h3memo[3][1] = 1
h3memo[3][2] = 0
h3memo[3][3] = 1
h3memo[3][4] = 3
h3memo[3][5] = 2
h3memo[3][6] = 1
h3memo[3][7] = 2
h3memo[3][8] = 4
h3memo[3][9] = 3
h3memo[3][10] = 2
h3memo[3][11] = 3
h3memo[3][12] = 5
h3memo[3][13] = 4
h3memo[3][14] = 3
h3memo[3][15] = 4
h3memo[4][0] = 3
h3memo[4][1] = 2
h3memo[4][2] = 1
h3memo[4][3] = 0
h3memo[4][4] = 4
h3memo[4][5] = 3
h3memo[4][6] = 2
h3memo[4][7] = 1
h3memo[4][8] = 5
h3memo[4][9] = 4
h3memo[4][10] = 3
h3memo[4][11] = 2
h3memo[4][12] = 6
h3memo[4][13] = 5
h3memo[4][14] = 4
h3memo[4][15] = 3
h3memo[5][0] = 4
h3memo[5][1] = 3
h3memo[5][2] = 2
h3memo[5][3] = 1
h3memo[5][4] = 3
h3memo[5][5] = 2
h3memo[5][6] = 1
h3memo[5][7] = 0
h3memo[5][8] = 4
h3memo[5][9] = 3
h3memo[5][10] = 2
h3memo[5][11] = 1
h3memo[5][12] = 5
h3memo[5][13] = 4
h3memo[5][14] = 3
h3memo[5][15] = 2
h3memo[6][0] = 5
h3memo[6][1] = 4
h3memo[6][2] = 3
h3memo[6][3] = 2
h3memo[6][4] = 4
h3memo[6][5] = 3
h3memo[6][6] = 2
h3memo[6][7] = 1
h3memo[6][8] = 3
h3memo[6][9] = 2
h3memo[6][10] = 1
h3memo[6][11] = 0
h3memo[6][12] = 4
h3memo[6][13] = 3
h3memo[6][14] = 2
h3memo[6][15] = 1
h3memo[7][0] = 6
h3memo[7][1] = 5
h3memo[7][2] = 4
h3memo[7][3] = 3
h3memo[7][4] = 5
h3memo[7][5] = 4
h3memo[7][6] = 3
h3memo[7][7] = 2
h3memo[7][8] = 4
h3memo[7][9] = 3
h3memo[7][10] = 2
h3memo[7][11] = 1
h3memo[7][12] = 3
h3memo[7][13] = 2
h3memo[7][14] = 1
h3memo[7][15] = 0
h3memo[8][0] = 5
h3memo[8][1] = 4
h3memo[8][2] = 3
h3memo[8][3] = 4
h3memo[8][4] = 4
h3memo[8][5] = 3
h3memo[8][6] = 2
h3memo[8][7] = 3
h3memo[8][8] = 3
h3memo[8][9] = 2
h3memo[8][10] = 1
h3memo[8][11] = 2
h3memo[8][12] = 2
h3memo[8][13] = 1
h3memo[8][14] = 0
h3memo[8][15] = 1
h3memo[9][0] = 4
h3memo[9][1] = 3
h3memo[9][2] = 4
h3memo[9][3] = 5
h3memo[9][4] = 3
h3memo[9][5] = 2
h3memo[9][6] = 3
h3memo[9][7] = 4
h3memo[9][8] = 2
h3memo[9][9] = 1
h3memo[9][10] = 2
h3memo[9][11] = 3
h3memo[9][12] = 1
h3memo[9][13] = 0
h3memo[9][14] = 1
h3memo[9][15] = 2
h3memo[10][0] = 3
h3memo[10][1] = 4
h3memo[10][2] = 5
h3memo[10][3] = 6
h3memo[10][4] = 2
h3memo[10][5] = 3
h3memo[10][6] = 4
h3memo[10][7] = 5
h3memo[10][8] = 1
h3memo[10][9] = 2
h3memo[10][10] = 3
h3memo[10][11] = 4
h3memo[10][12] = 0
h3memo[10][13] = 1
h3memo[10][14] = 2
h3memo[10][15] = 3
h3memo[11][0] = 2
h3memo[11][1] = 3
h3memo[11][2] = 4
h3memo[11][3] = 5
h3memo[11][4] = 1
h3memo[11][5] = 2
h3memo[11][6] = 3
h3memo[11][7] = 4
h3memo[11][8] = 0
h3memo[11][9] = 1
h3memo[11][10] = 2
h3memo[11][11] = 3
h3memo[11][12] = 1
h3memo[11][13] = 2
h3memo[11][14] = 3
h3memo[11][15] = 4
h3memo[12][0] = 1
h3memo[12][1] = 2
h3memo[12][2] = 3
h3memo[12][3] = 4
h3memo[12][4] = 0
h3memo[12][5] = 1
h3memo[12][6] = 2
h3memo[12][7] = 3
h3memo[12][8] = 1
h3memo[12][9] = 2
h3memo[12][10] = 3
h3memo[12][11] = 4
h3memo[12][12] = 2
h3memo[12][13] = 3
h3memo[12][14] = 4
h3memo[12][15] = 5
h3memo[13][0] = 2
h3memo[13][1] = 1
h3memo[13][2] = 2
h3memo[13][3] = 3
h3memo[13][4] = 1
h3memo[13][5] = 0
h3memo[13][6] = 1
h3memo[13][7] = 2
h3memo[13][8] = 2
h3memo[13][9] = 1
h3memo[13][10] = 2
h3memo[13][11] = 3
h3memo[13][12] = 3
h3memo[13][13] = 2
h3memo[13][14] = 3
h3memo[13][15] = 4
h3memo[14][0] = 3
h3memo[14][1] = 2
h3memo[14][2] = 1
h3memo[14][3] = 2
h3memo[14][4] = 2
h3memo[14][5] = 1
h3memo[14][6] = 0
h3memo[14][7] = 1
h3memo[14][8] = 3
h3memo[14][9] = 2
h3memo[14][10] = 1
h3memo[14][11] = 2
h3memo[14][12] = 4
h3memo[14][13] = 3
h3memo[14][14] = 2
h3memo[14][15] = 3
h3memo[15][0] = 4
h3memo[15][1] = 3
h3memo[15][2] = 2
h3memo[15][3] = 3
h3memo[15][4] = 3
h3memo[15][5] = 2
h3memo[15][6] = 1
h3memo[15][7] = 2
h3memo[15][8] = 2
h3memo[15][9] = 1
h3memo[15][10] = 0
h3memo[15][11] = 1
h3memo[15][12] = 3
h3memo[15][13] = 2
h3memo[15][14] = 1
h3memo[15][15] = 2
    
class Peca():
    def __init__(self, tabuleiro, indexZero, g = 0):
        self.tabuleiro = tabuleiro
        self.indexZero=indexZero
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
    return entrada,get_indexInicio(entrada)

def heuristicaUm(tabuleiro):
    count=0
    for a in range(0,16):
        if tabuleiro[a]!=tabuleiroFinal[a]:
            count+=1
    return count


def Spiral(matriz):
    return matriz and list(matriz.pop(0)) + Spiral(zip(*matriz)[::-1])      #->Python 2
    #return matriz and [*matriz.pop(0)] + Spiral([*zip(*matriz)][::-1])     #->Python 3

def heuristicaDois(tabuleiro):
    caracol=list(range(0,16))
    count=0
    aux=0
    mat=[]
    for i in range(4):
        mat.append([]) 
        for j in range(4):
            mat[i].append(tabuleiro[aux])
            aux+=1         
    caracol=Spiral(mat)  
    for ind,item in enumerate(caracol):
        if ind > 0 and ind < 14:
            if caracol[ind +1] != item + 1:
                count += 1
    return count

def heuristicaTres(tabuleiro):
    resp = 0
    for i in range(16):
        if (tabuleiro[i] != 0):
            resp += h3memo[tabuleiro[i]][i] 
    return resp

def heuristicaQuatro(tabuleiro):
    h1=heuristicaUm(tabuleiro)
    h2=heuristicaDois(tabuleiro)
    h3=heuristicaTres(tabuleiro)
    return int(0.1 * (h1) + 0.05 *(h2) + 0.85 * (h3))

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
    auxOpen={}
    heapq.heappush(listaAberta, noI)
    selecionado = heapq.heappop(listaAberta)
    while selecionado.tabuleiro != tabuleiroFinal:
        listaFechada.add(selecionado.tabuleiro)
        
        for new_tabuleiro, indexZero in geraSucessores(selecionado):
            filho=Peca(new_tabuleiro,indexZero,selecionado.g+1)

            if hash(new_tabuleiro) in auxOpen:

                if filho < auxOpen.get(hash(new_tabuleiro)):
                    continue    
            
            if new_tabuleiro not in listaFechada:    
                heapq.heappush(listaAberta,filho)
                auxOpen[hash(new_tabuleiro)] = filho
        
        selecionado = heapq.heappop(listaAberta) 
    print(f"{psutil.Process().memory_info().rss * 0.000001} megabites")
    print(f"{time.process_time() - start } segundos")
    return selecionado.g


def main():
    inicial,ind0 = readInput()
    pecaInicio = Peca(inicial,ind0)
    resultado = AEstrela(pecaInicio)
    print(resultado)
if __name__ == '__main__':
    main()
