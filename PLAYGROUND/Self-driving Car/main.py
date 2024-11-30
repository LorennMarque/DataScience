import sys
from train_agent import main as train
from test_agent import main as test

if __name__ == "__main__":
    print("Selecciona una opción:")
    print("1: Entrenar al agente")
    print("2: Probar al agente")

    option = input("Opción: ")
    if option == "1":
        train()
    elif option == "2":
        test()
    else:
        print("Opción inválida.")
        sys.exit(1)
