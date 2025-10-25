from typing_extensions import Self


class Luz:
    def ligar(self: Self):
        print("Luz ligada")

    def desligar(self: Self):
        print("Luz desligada")

class ControleRemoto:
    def __init__(self: Self, luz: Luz):
        self.luz = luz

    def apertarBotaoLigar(self: Self):
        self.luz.ligar()

    def apertarBotaoDesligar(self: Self):
        self.luz.desligar()

if __name__ == "__main__":
    luz = Luz()
    controle = ControleRemoto(luz)

    controle.apertarBotaoLigar()
    controle.apertarBotaoDesligar()
