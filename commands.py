from typing_extensions import Self
from interfaces import Command
from luz import Luz

class LigarLuz(Command):
    def __init__(self: Self, luz: Luz):
        self.luz = luz

    def execute(self: Self):
        self.luz.ligar()

class DesligarLuz(Command):
    def __init__(self: Self, luz: Luz):
        self.luz = luz

    def execute(self: Self):
        self.luz.desligar()

class ControleRemoto():
    def __init__(self: Self):
        self.command = Command

    def setCommand(self, command: Command):
        self.command = command

    def apertarBotao(self):
        self.command.execute()
