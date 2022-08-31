
# Alessa Baptista dos Santos
#GitHub: GingerLeh
#----------------------------------------------#------------------------------------------------------#
class Horario: 
    def  __init__(self,hora:int,minuto:int):
        self.hora = hora
        self.minuto = minuto

    def incrementaUmMinuto(self):
        if self.minuto + 1 >= 60:
            self.incrementaUmaHora()
            self.minuto = 00

        else:
            self.minuto+=1

    def decrementaUmMinuto(self):
        if self.minuto == 00:
            self.decrementaUmaHora()
            self.minuto = 59

        else:
            self.minuto-=1

    def incrementaUmaHora(self):
        if self.hora + 1 >= 24:
            self.hora = 00
        else:
            self.hora+=1

    def decrementaUmaHora(self):
        if self.hora == 0:
            self.hora = 23
        else:
            self.hora-=1

    def mostraHorario(self):
        return print('%02d:%02d'%(self.hora,self.minuto))

    def verificaPeriodo(self):
        if self.hora >=12 and self.hora<=00:
            return print('PM')
        else:
            return print('AM')

horario= Horario(12,45)
horario2= Horario(23,00)
horario3= Horario(23,59)

# horario.incrementaUmaHora()
# horario.decrementaUmaHora()
# horario.incrementaUmMinuto()
# horario.decrementaUmMinuto()

# horario2.incrementaUmaHora()
# horario2.decrementaUmaHora()
# horario2.incrementaUmMinuto()
# horario2.decrementaUmMinuto()

horario3.incrementaUmaHora()
horario3.mostraHorario()
horario3.decrementaUmaHora()
horario3.mostraHorario()
horario3.incrementaUmMinuto()
horario3.mostraHorario()
horario3.decrementaUmMinuto()
horario3.mostraHorario()

#----------------------------------------------#------------------------------------------------------#
