
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        # dois underlines(__) são como contrutores no python
        # self é a memoria da referencia criada pelo python função construtora
        # para deixar o atributo privado se usa underlines(__)
        # _Conta__numero classe e o atributo agora é privado mexer apenas por metodos
        # @property para getter e @atributo.setter para setter ex. (@nome.setter)

        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

#metodos
    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite. ".format(valor))

    def extrato(self):
        print("Seu saldo atual é: R$ {}".format(self.__saldo))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_para_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_para_sacar

#getters e setters
    """def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    def get_limite(self):
        return self.__limite
    
    #def set_limite(self, limite):
    #    self.__limite = limite """

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite


    @limite.setter
    def limite(self, limite):
        self.__limite = limite

#metodos da CLASSE estaticos

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}