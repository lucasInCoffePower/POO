"""
    Módulo com função principal do programa
"""

#   importando modulo "conta.py"
from encapsulamento.exercicio.conta_bancaria.classe_conta.conta import ContaBancaria


def main():
    """
        Funçãoq principal
        Responsável por imprimir na tela
    """

    c1 = ContaBancaria("Daniel Silva", 45, "15151561515") # Criando objeto
    print(c1) # mostrando objeto
    print(c1.saldo) # verificando o valor no atributo saldo
    c1.deposito(500) # Adicionanod saldo a conta
    print(c1.saldo) # Verificando o taldo tm
    c1.titular = "João"
    print(c1)

if __name__ == '__main__':
    main()