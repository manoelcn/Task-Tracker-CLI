import sys

from services import (
    add_task,
    list_tasks,
    task_delete,
    task_mark_status,
    task_update,
)

HELP_MESSAGE = """
Task Tracker CLI - List of Commands:

Commands:
  add <descrição>             Add a new task
  update <id> <descrição>     Update the description of an existing task
  delete <id>                 Delete a task
  mark-in-progress <id>       Mark a task as in progress
  mark-done <id>              Mark a task as completed
  list                        List all tasks
  --help                      Display this help message
"""

def main():
    if len(sys.argv) <= 1 or sys.argv[1] == '--help':
        print(HELP_MESSAGE)
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == 'add':
        if not args:
            print('Please provide a description for the task.')
            return
        description = ' '.join(args)
        add_task(description)

    elif command == 'update':
        if not args:
            print('Please provide a task ID.')
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
            print('Please provide a task ID.')
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
            print('Please provide a task ID.')
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
            print('Please provide a task ID.')
            return
        status = 'in-progress'
        try: 
            task_id = int(args[0])
        except ValueError:
            print("ID must be a number.")
            return
        task_mark_status(task_id, status)

    else:
        print(HELP_MESSAGE)


if __name__ == '__main__':
    main()
