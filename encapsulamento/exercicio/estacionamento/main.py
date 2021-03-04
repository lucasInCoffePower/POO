"""
    Modulo com função principal
"""
from encapsulamento.exercicio.estacionamento.modulos.classe_estacionamento import Estacionamento


def main():
    """
        Funcao que imprimi na tela
    """

    p = Estacionamento()
    print(p.entrar())
    print(p.entrar())
    print(p.entrar())
    print(p.sair())
    print(p)


if __name__ == '__main__':
    main()
