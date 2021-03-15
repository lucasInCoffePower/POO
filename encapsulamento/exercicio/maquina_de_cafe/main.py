"""
    Módulo "main"
    Contém a função principal
"""

from encapsulamento.exercicio.maquina_de_cafe.modulo.classe_cafeteira import Cafeteira


def main():
    """
        Função principal
    """
    C1 = Cafeteira()
    print(C1)
    print(C1.dez())
    print(C1.dez())
    print(C1.dez())
    print(C1.dez())
    print(C1.cinco())
    print(C1.dez())
    print(C1)
    print(C1.retirar_cafe())
    print(C1)
    print(C1.retirar_troco())
    print(C1)
    print(C1.retirar_cafe())
    print(C1)


if __name__ == '__main__':
    main()
