import sys
import saludador.modules.examples.saludador as saludador
import saludador.launcher.__version__ as __version__
import saludador.modules.files as files

from termcolor import colored

def main():
    print("[", colored("Iniciando app de pruebas", "green"), f"] ver: {__version__}")
    print("- modulo saludador:", saludador.saluda_a("jaime"))
    print(colored("* Abriendo archvio desde resoruces/texts/archivo.txt:", "light_grey"))
    files.read_file("resources/textos/archivo.txt")
     
if __name__ == "__main__":
    sys.exit(main())
