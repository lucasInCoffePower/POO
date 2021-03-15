"""
    Módulo com a classe Cafeteira
"""


class Cafeteira:
    """
        Abstrai as características e comportamentos de uma cafeteira
    """

    def __init__(self, valor_cafe=0.50):
        """
            Construtor da cafeteira
            Recebe um tipo float para valor_cafe : valor do cafe
        """
        self._valor_cafe = valor_cafe  # preço do café
        self._valor_total = 0.0  # total de dinheiro na máquina
        self._troco = 0.0
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
            Preço do café {self._valor_cafe}
            Dinheiro do usuário {self._valor_total}
            Café: {status}
            Troco: {self._troco}
            '''

    def _conferir_valor(self):
        """
            Método que confere se o valor na máquina não é maior que o do café
        """
        self._status = True if self._valor_total >= self._valor_cafe
        return self._status

    def cinco(self, valor = 0.5):
        """
            Método que simula a entrada de uma moeda de 5 centavos
        """
        if not(self._conferir_valor()):
            self._valor_total += valor
            return True
        else:
            return False


    def dez(self, valor = 0.10):
        """
            Método que simula o entrada de uma moeda de 10 centavos
        """
        if not(self._conferir_valor()):
            self._valor_total += valor
            return True
        else:
            return False


    def verificar_troco(self):
        """
            Método que verifica se há troco
            Retorna um tipo bool: True, se há troco; False, se não há troco
        """
        if (self._valor_total - self._valor_cafe) > 0:
            return True
        else:
            return False

    def retirar_troco(self):
        """
            Método que retira o troco
            Retorna um tipo float:
        """
        return self._troco

