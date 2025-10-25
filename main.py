from commands import ControleRemoto, DesligarLuz, LigarLuz
from luz import Luz


if __name__ == "__main__":
    luz = Luz()

    ligar = LigarLuz(luz)
    desligar = DesligarLuz(luz)

    controle = ControleRemoto()

    controle.setCommand(ligar)
    controle.apertarBotao()

    controle.setCommand(desligar)
    controle.apertarBotao()