"""
    Módulo com classe ContaBancari
"""


class ContaBancaria:
    """
        Classe que abstrai características de uma conta bancária
    """

    def __init__(self, nome, idade, cpf):
        """
            :param nome: recebe um tipo string
            :param idade: recebe um tipo int
            :param cpf:  recebe um tipo string
        """

        self._titular = nome
        self._idade = idade
        self._cpf = cpf
        self._saldo = 0

    @property
    def titular(self):
        """
                Função que retorn o titular da conta
            """
        return self._titular

    @property
    def idade(self):
        """
            Função que retorna a idade do titular
        """

        return self._idade

    @property
    def cpf(self):
        """
            Função que retorna o cpf do titular
        """

        return self._cpf

    @property
    def saldo(self):
        """
            Função que retorna o saldo
        """
        return self._saldo

    @titular.setter
    def titular(self, nome):
        """
            Função que altera o nome do titular da conta
            Recebe um tipo str para nome
        """
        self._titular = nome

    def saque(self, valor):
        """
            Funçãq que representa o saque
            Recebe um tipo float para 'valor': valor do saque
        """

        if self._saldo >= valor:
            self._saldo -= valor
            return f"saque efetuado"
        else:
            return f"saldo insuficiente"

    def deposito(self, valor):
        """
            Função que representa um depósito
            Recebe um tipo float para 'valor': valor do depósito
        """

        if valor > 0:
            self._saldo += valor
            return "deposito efetuado"
        else:
            return "deposito inválido"

    def __str__(self):
        """
            Função que retorna uma representação em string do objeto
        """

        return f"""
                Conta Bancaria
                \tTitular: {self._titular}
                \tSaldo: R$ {self._saldo}                    
                """


def main():
    """
        Função resposável por imprimir
    """


if __name__ == '__main__':
    main()
