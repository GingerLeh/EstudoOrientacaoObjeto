# Alessa Baptista dos Santos
# Ra: 10483121089
#----------------------------------------------#------------------------------------------------------#
import random
import numpy as np
#---------------------------------------------#------------------------------------------------------#
class Voo:
    def __init__(self,numVoo:int,horarioVoo:str,assentosLivres=None):
        self.numVoo = numVoo
        self.horarioVoo = horarioVoo
        self.assentosLivres= assentosLivres
        self.geraAssentos()
        
    def geraAssentos(self):
        self.assentosLivres = np.zeros(100)
    
    def getProximoAssento(self):
        for i, v in enumerate(self.assentosLivres): 
            if v == 0:
                return print(f'O lugar mais próximo vago é: {i}º')

    def verificarAssentoLivre(self,numAssento):
        if self.assentosLivres[numAssento]==0:
            return True
        else:
            return False

    def ocuparAssento(self, numAssento, flag=None):
        if self.assentosLivres[numAssento] == 0:
            self.assentosLivres[numAssento]=1
            if flag == None:
                print(f'O lugar {numAssento} foi ocupado,obrigado')
        else:
            if flag == None:
                print('Assento ocupado! Tente outro')
    
    def getVagas(self):
        contador = 0
        for i in self.assentosLivres:
            if i == 0:
                contador+=1
        return print(f'Existem {contador} lugares livres')

    def getVoo(self):
        print(f'O número do voo é: {self.numVoo}')

    def getHoraVoo(self):
        print(f'A hora do voo é {self.horarioVoo}')

    def getMapaAssentos(self):
        print(' /',self.assentosLivres[0:24])
        print('/|',self.assentosLivres[25:49])
        print('\\|',self.assentosLivres[50:74])
        print(' \\',self.assentosLivres[75:99])
    
voo = Voo(4562,'12:45')

#ocupando os assentos de forma randomica:
for i in range(50):
    numero = random.randint(0,99)
    voo.ocuparAssento(numero,flag=1)

voo.getMapaAssentos()
voo.getVagas()
print(voo.verificarAssentoLivre(45))
voo.getVoo()
voo.getHoraVoo()
voo.getProximoAssento()
voo.ocuparAssento(3)
voo.getMapaAssentos()


#----------------------------------------------#------------------------------------------------------#
