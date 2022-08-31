# Alessa Baptista dos Santos
#GitHub: GingerLeh
#----------------------------------------------#------------------------------------------------------#
class CodigoPostal: 
    def __init__(self, indicativo:str,extensao:str,rua:str):
        self.indicativo = indicativo
        self.extensao = extensao
        self.rua = rua
    
    def mostrar(self):
        if len(self.indicativo)==5 and len(self.extensao)==3 and self.indicativo.isdigit() and self.extensao.isdigit():
            print(self.indicativo, '-',self.extensao,' ',self.rua)
        else:
            print('Cep está com tamanho inapropriado!')



rua1 = CodigoPostal(indicativo='12345',extensao='123',rua='Rua do Sol')
rua2 = CodigoPostal('12332','223','Rua das Oliveiras')
rua3 = CodigoPostal('1234578','12323','Rua da Morada')
rua4 = CodigoPostal('3332A','144','Rua dos Aspargos')
rua5 = CodigoPostal('11233','3344','Avenida da Saudade')
rua6 = CodigoPostal('190223','223','Avenida Brasil')

rua1.mostrar()
# rua3.mostrar()
rua4.mostrar()
# rua5.mostrar()
# rua6.mostrar()
# rua2.mostrar()
#----------------------------------------------#------------------------------------------------------#
