import random
import seaborn as sns

class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10, 100) if i % 2 == 0]
        self.porta_halteres = {}
        self.reiniciar_o_dia()
    
    def reiniciar_o_dia(self):
        self.porta_halteres = {i: i for i in self.halteres}

    def listar_halteres(self):
        return [i for i in self.porta_halteres.values() if i != 0]
    
    def pegar_halter(self, peso):
        halt_pos = list(self.porta_halteres.values()).index(peso)
        key_halt = list(self.porta_halteres.keys())[halt_pos]
        self.porta_halteres[key_halt] = 0
        return peso
    
    def listar_espaços(self):
        return [i for i,j in self.porta_halteres.items() if j == 0]
    
    def devolver_halter(self, pos, peso):
        self.porta_halteres[pos] = peso

    def calcular_caos(self):
        num_caos = [i for i,j in self.porta_halteres.items() if i != j]
        return len(num_caos) / len(self.porta_halteres)
    
class Usuario:
    def __init__(self, tipo, academia):
        self.tipo = tipo # 1 - normal | 2 - bagunceiro
        self.academia = academia
        self.peso = 0

    def iniciar_treino(self):
        lista_pesos = self.academia.listar_halteres()
        self.peso = random.choice(lista_pesos)
        self.academia.pegar_halter(self.peso)

    def finalizar_treino(self):
        pos_disp = self.academia.listar_espaços()

        if (self.tipo == 1) and (self.peso in pos_disp):
            self.academia.devolver_halter(self.peso, self.peso)
        else:
            pos_entrega = random.choice(pos_disp)
            self.academia.devolver_halter(pos_entrega, self.peso)
        
        self.peso = 0


academia = Academia()   
usuarios = [Usuario(1, academia) for i in range(10)]
usuarios += [Usuario(2, academia) for i in range(1)]

random.shuffle(usuarios)

usuarios[1].iniciar_treino()

caos_list = list()
for i in range(1000):
    academia.reiniciar_o_dia()
    for i in range(10):
        random.shuffle(usuarios)
        for user in usuarios:
            user.iniciar_treino()
        for user in usuarios:
            user.finalizar_treino()
    caos_list.append(academia.calcular_caos())

def calcular_media(lista):
    soma = 0
    for i in lista:
        soma += i
    
    return soma / len(lista)

calcular_media(caos_list)

sns.displot(caos_list)