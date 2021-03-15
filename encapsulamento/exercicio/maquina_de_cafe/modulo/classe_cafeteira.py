"""
    Módulo com a classe Cafeteira
"""
import self as self


class Cafeteira:
    """
        Abstrai as características e o comportamento de uma cafeteira
    """

    def __init__(self, valor_cafe=0.50):
        """
            Construtor da cafeteira
            Recebe um tipo float para valor_cafe : valor do cafe
        """
        self._valor_cafe = valor_cafe  # preço do café
        self._valor_total = 0.0  # total de dinheiro na máquina
        self._troco = 0.0  # troco do usuário
        self._status = False  # status de disponibilidade de café na máquina

    def __str__(self):
        """
            Método que retorna as características do objeto como string
        """
        status = "Café Pronto" if self._status else "Sem Café"

        return f'''
            ------------------------
            Máquina de Café
            ------------------------
            Preço do café: R$ {self._valor_cafe}
            Dinheiro do usuário: R$ {self._valor_total}
            Café: {self._status}
            Troco: R$ {self._troco}
            '''

    @property
    def valor_cafe(self):
        """
            Método que mostra o valor do cafe
            Retorna um tipo str: valor do café
        """
        return f"R$ {self._valor_cafe}"

    @valor_cafe.setter
    def valor_cafe(self, valor):
        """
            Método que altera o valor do café
            Recebe um tipo float para valor: novo valor do café
        """
        self._valor_cafe = valor

    def _conferir_valor(self, valor):
        """
            Método que confere se o valor na máquina não é maior ou igual que o do café
            Retorna um tipo boolean: True, se o valor é maior ou igual; False, se ainda não é o valor do café
        """
        if not self._status:
            if self._valor_total + valor >= self._valor_cafe:
                self._troco = round(self._valor_total + valor - self._valor_cafe,2)
                self._status = True
            return False
        else:
            return True

    @property
    def valor_total(self):
        """
            Método que retorna o valor inserido na máquina
            Retorna um tipo float: valor total inserido pelo usuário na máquina
        """
        return self._valor_total

    def cinco(self, valor=0.05):
        """
            Método que simula a entrada de uma moeda de 5 centavos
            Retorna um tipo boolean: True, se o depósito foi aceito; False, se o depósito não foi aceito
        """
        if not (self._conferir_valor(valor)):
            self._valor_total += valor
            return True
        else:
            return False

    def dez(self, valor=0.10):
        """
            Método que simula o entrada de uma moeda de 10 centavos
            Retorna um tipo boolean: True, se o depósito foi aceito; False, se o depósito não foi aceito
        """
        if not (self._conferir_valor(valor)):
            self._valor_total += valor
            return True
        else:
            return False

    def verificar_troco(self):
        """
            Método que verifica se há troco
            Retorna um tipo bool: True, se há troco; False, se não há troco
        """
        if self._troco > 0:
            return True
        else:
            return False

    def retirar_troco(self):
        """
            Método que retira o troco
            Retorna um tipo float: valor do troco
        """
        if self.verificar_troco():
            valor = self._troco
            self._troco = 0.0
            return valor
        else:
            return 0.0

    def retirar_cafe(self):
        """
            Método que simula a função de retirar café
            Retorna uma string indicando a retirada do café ou a impossibilidade de retirar
        """
        if self._status and not(self.verificar_troco()):
            self._valor_total = 0.0
            self._status = False
            return "Café retirado"
        else:
            return "Sem Café para retirar ou ainda há troco para retirar"

    @property
    def troco(self):
        """
            Método que retorna o valor do troco
            Retorna um str: valor do troco
        """
        return f"R$ {self._troco}"
