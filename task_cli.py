import sys
from task_manager import add_task


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
        add_task(description)

    else:
        print("Comando inválido")


if __name__ == "__main__":
    main()
