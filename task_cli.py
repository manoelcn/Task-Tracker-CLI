import sys
from task_manager import add_task, list_tasks, task_mark_status, task_update


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

    if command == "update":
        if not args:
            print('Sem argumentos')
            return
        description = ' '.join(args)
        task_update(int(args[0]) ,description)

    elif command == 'list':
        list_tasks()

    elif command == 'mark-done':
        if not args:
            print('Sem argumentos')
            return
        status = 'done'
        task_mark_status(int(args[0]), status)

    elif command == 'mark-in-progress':
        if not args:
            print('Sem argumentos')
            return
        status = 'in-progress'
        task_mark_status(int(args[0]), status)

    else:
        print("Comando inválido")

if __name__ == "__main__":
    main()
