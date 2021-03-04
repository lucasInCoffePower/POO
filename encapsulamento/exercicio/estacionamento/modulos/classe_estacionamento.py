"""
    Módulo com a classe estacionamento
"""


class Estacionamento():
    """
        Classe que abstrai caracteristicas de um estacionamento
    """

    def __init__(self, capacidade = 50, vagas=50):
        """
            Inicialização do construtor
            Recebe um tipo int para vagas: capacidade do estacionamento
        """
        self._capacidade = capacidade # atributos protegidos
        self._vagas = vagas # atributos protegidos

    """
        Declaracao dos métodos comportamentais
    """

    def entrar(self):
        """
            Recebe um tipo Carro: para carro
        """

        if self._vagas >= 0:
            self._vagas -= 1
            return "Um carro entrou"
        else:
            return "Lotado"

    def sair(self):
        """
            Função que indica a saida de um carro
        """
        if self._vagas != 0:
            self._vagas += 1
            return "Carro saiu"
        else:
            return "Não há carros no estacionamento"

    def __str__(self):
        """
            Função que retorn o estacionamento em string
        """
        return f"Capacidade: {self._capacidade}/Vagas: {self._vagas}"

    @property
    def vagas(self):
        """
            Função que mostra a quantidade de vagas sobrenao no estacionamento

        """
        return self._vagas

    @property
    def capacidade(self):
        """
            Função que retorna a capacidade da classe
        """

        return self._capacidade

def main():
    """
        Função que imprime na tela
    """


if __name__ == '__main__':
    main()
