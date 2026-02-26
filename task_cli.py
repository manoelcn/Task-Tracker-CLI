import sys


def main():
    if len(sys.argv) <= 1:
        print('Nenhum comando foi informado.')
        return

    command = sys.argv[1]
    args = sys.argv[2:]
    if command == "add":
        if not args:
            print('Sem argumentos')
            return
        description = ' '.join(args)
        print("Função add será chamada")
        print(f'Argumentos: {description}')
    else:
        print("Comando inválido")


if __name__ == "__main__":
    main()
