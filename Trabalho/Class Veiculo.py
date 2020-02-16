class abstract Veiculo :
    def  __init__(self, codigo, placa, modelo, valorBase):
        self.codigo = codigo
        self.placa = placa
        self.modelo = modelo
        self.valorBase = valorBase

    def  __str__(self):
        return u '{} - {} - {} - {}'.format(self.codigo,self.placa,self.modelo,self.valorBase)

    def abstract valordaDiaria(self):
        

class VeiculoPolular(Veiculo):

    def  __init__(self):

    def valordaDiaria(self):
        return self.valorBase

class VeiculoUtilitario(Veiculo):

    def  __init__(self):

    def valordaDiaria(self):
        return self.valorBase*1.3

class VeiculoEsportivo(Veiculo):

    def  __init__(self):

    def valordaDiaria(self):
        return self.valorBase*1.5
