import sys

from services import (
    add_task,
    list_tasks,
    task_delete,
    task_mark_status,
    task_update,
)


def main():
    if len(sys.argv) <= 1:
        print('Nenhum comando foi informado.')
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == 'add':
        if not args:
            print('Sem argumentos')
            return
        description = ' '.join(args)
        add_task(description)

    elif command == 'update':
        if not args:
            print('Sem argumentos')
            return
        description = ' '.join(args)
        try: 
            task_id = int(args[0])
        except ValueError:
            print("ID must be a number.")
            return
        task_update(task_id, description)

    elif command == 'delete':
        if not args:
            print('Sem argumentos')
            return
        try: 
            task_id = int(args[0])
        except ValueError:
            print("ID must be a number.")
            return
        task_delete(task_id)

    elif command == 'list':
        list_tasks()

    elif command == 'mark-done':
        if not args:
            print('Sem argumentos')
            return
        status = 'done'
        try: 
            task_id = int(args[0])
        except ValueError:
            print("ID must be a number.")
            return
        task_mark_status(task_id, status)

    elif command == 'mark-in-progress':
        if not args:
            print('Sem argumentos')
            return
        status = 'in-progress'
        try: 
            task_id = int(args[0])
        except ValueError:
            print("ID must be a number.")
            return
        task_mark_status(task_id, status)

    else:
        print('Comando inválido')


if __name__ == '__main__':
    main()
